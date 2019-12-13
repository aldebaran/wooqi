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
    if global_var['config'] is not None:
        # Filter and re-order tests
        sequencer_features.filter_order_tests(config, items)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    pytest_runtest_makereport hook
    """
    outcome = yield
    rep = outcome.get_result()
    if global_var['config'] is not None:
        result = 'Result : {}'.format(rep.outcome)

        # test_name according in file_config
        test_name = item.name.split('[')[0]
        if test_name not in global_var['config'].file_config:
            call_number = item.name.split('[')[1].split('-')[0].replace(']', '')
            test_name = '{}-{}'.format(test_name, call_number)

        # Add logs
        if call.when == 'setup':
            logger_gv.info('{} starts'.format(item.name))
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
                logger_gv.info("rerun {}".format(str(item)))
                if item.keywords.__dict__["reruns"] == global_var['config'].reruns(test_name) + 1:
                    skip = True
            else:
                skip = True

            # Manage the postfail feature according to the config test file
            sequencer_features.postfail_feature_management(item, skip)

        # Manage skip marker, when test fail on the teardown
        elif call.when == 'teardown' and rep.outcome == 'failed':
            logger_gv.error("Test teardown {}".format(result))

            if "reruns" in item.keywords.__dict__.keys():
                logger_gv.info("rerun {}".format(str(item)))
                if item.keywords.__dict__["reruns"] == global_var['config'].reruns(test_name) + 1:
                    skip = True
                else:
                    skip = False
            else:
                skip = True

            # Manage the postfail feature according to the config test file
            sequencer_features.postfail_feature_management(item, skip)


def pytest_report_header(config):
    """
    Beginning of the test
    """
    if config.getoption("--seq-config") is not None and config.getoption("--wooqi") is True:
        global_var['config'] = ConfigTest(config.getoption("--seq-config"))
        if global_var['config'].config_file_exists is False:
            print("\n")
            print("*****************************************************************")
            print("-- ERROR --")
            print("The config file {} doesn't exist".format(config.getoption('--seq-config')))
            print("*****************************************************************")
            print("\n")

        global_var['result'] = True
        if config.option.verbose > 0:
            return [""]
    else:
        global_var['config'] = None


def pytest_generate_tests(metafunc):
    """
    Generate test options
    """
    test_name = metafunc.function.__name__
    if global_var['config'] is not None:
        file_config = global_var['config'].file_config
        if test_name.startswith('test_') or test_name.startswith('action_'):

            test_used = False
            uut_list = []
            uut2_list = []
            sessions = []
            test_id = None
            for session in file_config:
                if session.split('-')[0] == test_name:
                    test_used = True
                    sessions.append(session)
                    # Manage paramaters
                    uuts, uuts2 = sequencer_features.get_uuts(session)
                    uut_list += uuts
                    uut2_list += uuts2

                    if '-' in session:
                        # Overwrite the test name according at configuration file
                        test_id = session.split('-')[1]
                        # The first addcall only rename the test name
                        metafunc.addcall(id=test_id)

            # Test not used
            if not test_used:
                return

            # Manage loop option
            if global_var['config'].loop_infos():
                for session in sessions:
                    loop_start, loop_stop = global_var['config'].loop_infos()[0]
                    loop_start_order = file_config[loop_start]['test_order']
                    loop_stop_order = file_config[loop_stop]['test_order']
                    test_order = file_config[session]['test_order']
                    if loop_start_order <= test_order <= loop_stop_order:
                        loop_iter = int(global_var['config'].loop_infos()[1])
                        if test_id is None:
                            for i in range(loop_iter):
                                metafunc.addcall(id='{}'.format(i))
                        else:
                            test_id = session.split('-')[1]
                            for i in range(loop_iter):
                                metafunc.addcall(id='{}-{}'.format(test_id, i))
                        file_config[session]['wooqi_loop_iter'] = loop_iter

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
    if global_var['config'] is not None:
        if logger_gv.init:
            logger_gv.debug('global result of the test')
        print("\n")
        if exitstatus == 0:
            if logger_gv.init:
                logger_gv.debug('---> passed')
            print('\n')
            print('ssssssss       ssss          ssssssss     ssssssss')
            print('ss    ss     ssss ssss       ssssssss     ssssssss')
            print('ss    ss    ssss   ssss      ss           ss')
            print('ss    ss   sssss   sssss     ss           ss')
            print('ssssssss   sssssssssssss     ssssssss     ssssssss')
            print('ss         sss       sss           ss           ss')
            print('ss         sss       sss           ss           ss')
            print('ss         sss       sss     ssssssss     ssssssss')
            print('ss         sss       sss     ssssssss     ssssssss')
        else:
            if logger_gv.init:
                logger_gv.debug('---> failed')
            print('\n')
            print('ssssssss       ssss             sss       s')
            print('ssssssss     ssss ssss          sss       ss')
            print('sss         ssss   ssss         sss       ss')
            print('sss        sssss   sssss        sss       ss')
            print('ssssssss   sssssssssssss        sss       ss')
            print('ssssssss   sss       sss        sss       ss')
            print('ss         sss       sss        sss       ss')
            print('ss         sss       sss        sss       ssssssss')
            print('ss         sss       sss        sss       ssssssss')

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

        text_insert = '{}\n'.format(config.getoption('--seq-config'))
        serial_number = config.getoption('--sn')
        cache_path = os.path.abspath('.cache/v/cache/{}'.format(serial_number))
        cache_file = open(cache_path, 'w')
        cache_file.write('{}{}'.format(text_insert, text))
        cache_file.close()
