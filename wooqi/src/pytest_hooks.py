# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Pytest hooks
"""
import os
import pytest
from wooqi.src import sequencer_features
from wooqi.src.config_test import ConfigTest
from wooqi.src import global_var
from wooqi.src import logger_gv


def pytest_collection_modifyitems(config, items):
    """
    Called after collection has been performed, filter and re-order
    the items in-place, and create global variable
    """
    if global_var['config'] != None:
        # Filter and re-order tests
        sequencer_features.filter_order_tests(config, items)

        # Configure the tests with the reruns and timeout features
        sequencer_features.configure_reruns_timeout_features(items)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    pytest_runtest_makereport hook
    """
    outcome = yield
    rep = outcome.get_result()
    if global_var['config'] != None:
        result = 'Result : %s' % rep.outcome
        test_name, item_args = sequencer_features.item_name_analyze(item.name)
        if global_var['config'].exist(test_name + "_0"):
            test_name = '%s_%s' % (test_name, item_args[0])

        # Add logs
        if call.when == 'setup':
            logger_gv.info('%s starts' % item.name)
            if 'skipped' in result:
                logger_gv.warning(result)

        # Manage skip marker, after test called or if test setup failed
        if call.when == 'call' or (call.when == 'setup' and rep.outcome == 'failed'):
            skip = False
            if "reruns" in item.keywords.__dict__.keys():
                item.keywords.__dict__["reruns"] = item.keywords.__dict__["reruns"] + 1
            if 'failed' in result:
                logger_gv.error(result)
            if 'skipped' in result:
                logger_gv.warning(result)
            if 'passed' in result:
                logger_gv.info(result)
            elif "reruns" in item.keywords.__dict__.keys():
                logger_gv.info("rerun " + str(item))
                if item.keywords.__dict__["reruns"] == global_var['config'].reruns(test_name) + 1:
                    skip = True
            else:
                skip = True

            if "loop" in item.keywords.__dict__["_markers"].keys():
                loop = True
            else:
                loop = False

            # Manage the postfail feature according to the config test file
            sequencer_features.postfail_feature_management(
                item.name, item, skip, loop)


def pytest_report_header(config):
    """
    Beginning of the test
    """
    if config.getoption("--seq-config") != None and config.getoption("--wooqi") is True:
        global_var['config'] = ConfigTest(config.getoption("--seq-config"))
        if global_var['config'].config_file_exists is False:
            print
            print "*****************************************************************"
            print "-- ERROR --"
            print "The config file %s doesn't exist" % config.getoption("--seq-config")
            print "*****************************************************************"
            print

        global_var['result'] = True
        if config.option.verbose > 0:
            return [""]
    else:
        global_var['config'] = None


def pytest_generate_tests(metafunc):
    """
    Generate test options
    """
    if global_var['config'] != None:
        # Test called one time
        if global_var['config'].exist(metafunc.function.__name__):
            # Manage loop option
            sequencer_features.init_loop_option(metafunc)
            # Get uut and uut2 when test is called
            uut_list, uut2_list = sequencer_features.get_uuts(metafunc)

        # Test called one time or more
        elif global_var['config'].exist('%s_0' % metafunc.function.__name__):
            metafunc.function.__dict__["add_call"] = True
            uut_list = []
            uut2_list = []
            cpt = 0
            while global_var['config'].exist('%s_%d' % (metafunc.function.__name__, cpt)):
                # Add call for each test performed
                metafunc.addcall()
                # Manage loop option
                sequencer_features.init_loop_option(metafunc, cpt)
                # Get uut and uut2 when test is called
                uuts = sequencer_features.get_uuts(metafunc, cpt)
                uut_list += uuts[0]
                uut2_list += uuts[1]
                cpt += 1

        # Test not used
        else:
            return

        # Add paramaters uut and uut2
        if uut_list:
            metafunc.function.__dict__["uut"] = True
            metafunc.parametrize("uut", list(set(uut_list)))
        if uut2_list:
            metafunc.parametrize("uut2", list(set(uut2_list)))


def pytest_sessionfinish(exitstatus, session):
    """
    whole test run finishes
    """
    if global_var['config'] != None:
        if logger_gv.init:
            logger_gv.debug('global result of the test')
        print "\n"
        if exitstatus == 0:
            if logger_gv.init:
                logger_gv.debug('---> passed')
            print
            print 'ssssssss       ssss          ssssssss     ssssssss'
            print 'ss    ss     ssss ssss       ssssssss     ssssssss'
            print 'ss    ss    ssss   ssss      ss           ss'
            print 'ss    ss   sssss   sssss     ss           ss'
            print 'ssssssss   sssssssssssss     ssssssss     ssssssss'
            print 'ss         sss       sss           ss           ss'
            print 'ss         sss       sss           ss           ss'
            print 'ss         sss       sss     ssssssss     ssssssss'
            print 'ss         sss       sss     ssssssss     ssssssss'
        else:
            if logger_gv.init:
                logger_gv.debug('---> failed')
            print
            print 'ssssssss       ssss             sss       s'
            print 'ssssssss     ssss ssss          sss       ss'
            print 'sss         ssss   ssss         sss       ss'
            print 'sss        sssss   sssss        sss       ss'
            print 'ssssssss   sssssssssssss        sss       ss'
            print 'ssssssss   sss       sss        sss       ss'
            print 'ss         sss       sss        sss       ss'
            print 'ss         sss       sss        sss       ssssssss'
            print 'ss         sss       sss        sss       ssssssss'

        if logger_gv.init:
            logger_gv.debug('===============================================')
            logger_gv.debug('================ END OF SCRIPT ================')
            logger_gv.debug('===============================================')


def pytest_unconfigure(config):
    """
    Copy cache file generate by pytest in new file with serial and config file
    """
    cache_path = os.path.abspath('.cache/v/cache/lastfailed')
    if os.path.isfile(cache_path):
        lastfailed_file = open(cache_path, 'r')
        text = lastfailed_file.read()
        lastfailed_file.close()

        text_insert = '%s\n' % config.getoption('--seq-config')
        serial_number = config.getoption('--sn')
        cache_path = os.path.abspath('.cache/v/cache/%s' % serial_number)
        cache_file = open(cache_path, 'w')
        cache_file.write(text_insert + text)
        cache_file.close()
