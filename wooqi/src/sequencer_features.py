# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Sequencer features
"""
import os
import time
import pytest
from wooqi.src import global_var


def get_uuts(pytest_metafunc, cpt=None):
    """
    Return uut and uut2 according to test
    """
    if cpt is None:
        test_name = pytest_metafunc.function.__name__
    else:
        test_name = '%s_%d' % (pytest_metafunc.function.__name__, cpt)
    uut = []
    uut2 = []
    if 'uut' in pytest_metafunc.fixturenames:
        uut += global_var['config'].uut(test_name)
    if 'uut2' in pytest_metafunc.fixturenames:
        uut2 += global_var['config'].uut2(test_name)
    return uut, uut2


def init_loop_option(pytest_metafunc, cpt=None):
    """
    Generate test call according to loop option
    """
    if global_var['config'].loop_infos() is not None:
        loop_tests = global_var['config'].loop_infos()[0]
        loop_iter = int(global_var['config'].loop_infos()[1])
        if cpt is None:
            test_name = pytest_metafunc.function.__name__
        else:
            test_name = '%s_%d' % (pytest_metafunc.function.__name__, cpt)
            # addcall function has already been used in the first loop
            loop_iter -= 1
        test_order = global_var['config'].file_config[test_name]['test_order']
        first_loop_test_order = global_var['config'].file_config[loop_tests[0]]["test_order"]
        last_loop_test_order = global_var['config'].file_config[loop_tests[1]]["test_order"]
        if first_loop_test_order <= test_order <= last_loop_test_order:
            pytest_metafunc.function.__dict__["add_call"] = True
            pytest_metafunc.function.__dict__["loop"] = True
            # Add call for each test performed after the first
            for nb in range(0, loop_iter):
                pytest_metafunc.addcall()


def configure_reruns_timeout_features(items):
    """
    Configure the tests with the reruns and timeout features
    according to the config test file
    """
    for item in items:
        test_name = item.name.split("[")[0]
        if global_var['config'].exist(test_name + "_0"):
            test_name = test_name + "_" + item.name.split("[")[1][0]
        if global_var['config'].exist(test_name):
            if global_var['config'].reruns(test_name) is not None:
                item.keywords.__dict__["reruns"] = 0
                item.add_marker(pytest.mark.flaky(
                    reruns=global_var['config'].reruns(test_name)))
            if global_var['config'].timeout(test_name) is not None:
                item.add_marker(pytest.mark.timeout(
                    global_var['config'].timeout(test_name)))


def item_name_analyze(item_name):
    """
    Return a basic test name and parameters
    """
    item_args = []
    if '[' not in item_name:
        test_basic_name = item_name
    else:
        # Create list with all args
        test_basic_name, parameters = item_name.split("[", 1)
        parameters = parameters.rsplit("]", 1)[0]
        # First character can to be '-' but not to be a separator
        previous_char_separator = True
        parameter = ''
        for index, char in enumerate(parameters):
            if previous_char_separator or char != '-':
                parameter += char
                previous_char_separator = False
            else:
                item_args.append(parameter)
                parameter = ''
                previous_char_separator = True
        item_args.append(parameter)

    return test_basic_name, item_args


def item_loop_option_analyse(item, test_name, first_arg):
    """
    Return config test name and the iteration number according to loop option
    """
    if "loop" in item.keywords.__dict__["_markers"].keys():
        # Test defined one time in config file
        if global_var['config'].exist(test_name):
            iter_number = int(first_arg)
        # Test defined multiple time in config file and is the first iteration
        elif global_var['config'].exist('%s_%s' % (test_name, first_arg)):
            iter_number = 0
            test_name = '%s_%s' % (test_name, first_arg)
        # Test defined multiple time in config file but not is the first iteration
        else:
            loop_tests = global_var['config'].loop_infos()[0]
            cpt = 0
            nb_test_in_loop = 0
            first_test_in_loop = None
            # Count the number of test defined in config file
            while global_var['config'].exist('%s_%d' % (test_name, cpt)):
                test_order = global_var['config'].file_config['%s_%d' %
                                                              (test_name, cpt)]['test_order']
                first_loop_test_order = global_var[
                    'config'].file_config[loop_tests[0]]["test_order"]
                last_loop_test_order = global_var['config'].file_config[loop_tests[1]]["test_order"]
                if first_loop_test_order <= test_order <= last_loop_test_order:
                    nb_test_in_loop += 1
                    if first_test_in_loop is None:
                        first_test_in_loop = cpt
                cpt += 1

            # Remove the number of test defined in config file
            call_number = int(first_arg) - cpt
            # Minimum iteraion is one
            iter_number = 1 + call_number // nb_test_in_loop
            # Found test_name in config file
            call_number = call_number % nb_test_in_loop + first_test_in_loop
            test_name = '%s_%d' % (test_name, call_number)
    else:
        iter_number = 0
        # If test_name exist first_arg is uut
        if not global_var['config'].exist(test_name):
            test_name = '%s_%s' % (test_name, first_arg)
    return test_name, iter_number


def filter_order_tests(config, items):
    """
    Filter and re-order the tests according to the config test file
    """
    list_temp = []
    list_loop_temp = []
    for item in items:
        basic_test_name, item_args = item_name_analyze(item.name)
        if not global_var['config'].exist(basic_test_name) and\
           not global_var['config'].exist(basic_test_name + "_0"):
            # Test not used
            continue

        if item_args:
            first_arg = item_args[0]
        else:
            first_arg = None
        config_test_name, iter_number = item_loop_option_analyse(item, basic_test_name, first_arg)

        # If len(item_args) is 1, item_args[0] is a uut and he exists
        if "add_call" in item.keywords.__dict__["_markers"].keys():
            uut_index = 1
        else:
            uut_index = 0
        if len(item_args) > uut_index:
            # Verify uut
            if item_args[uut_index] not in global_var['config'].uut(config_test_name):
                # uut not used for this test
                continue
            # Verify uut2
            if len(item_args) > 2:
                if item_args[uut_index + 1] not in global_var['config'].uut2(config_test_name):
                    # uut2 not used for this test
                    continue
        test_order = int(global_var['config'].file_config[config_test_name]['test_order'])
        if iter_number != 0:
            # Create second list only with test in loop option after the first iteration
            if not list_loop_temp:
                test_order_last_loop_test = global_var['config'].file_config[
                    global_var['config'].loop_infos()[0][1]]["test_order"]
                # Add a fake item who the test_oder is just after the last test of looping option
                list_temp.append([test_order_last_loop_test + 0.5, 'LOOP_TEST'])
            list_loop_temp.append([iter_number, test_order, item])
        else:
            list_temp.append([test_order, item])

    # Order items
    list_temp.sort()
    items_temp = []
    for item in list_temp:
        if str(item[1]).count('LOOP_TEST'):
            # Insert all tests of loop option instead of fake item
            list_loop_temp.sort()
            for loop_item in list_loop_temp:
                items_temp.append(loop_item[2])
        else:
            items_temp.append(item[1])
    items[:] = items_temp

    # Manage --failed-first option to pytest-cache for wooqi
    rerun_sequence_since_the_fail(config, items)


def rerun_sequence_since_the_fail(config, items):
    """
    To rerun sequence since the first fail
    """
    # Delete old cache file
    if not os.path.isdir(os.path.abspath('.cache/v/cache/')) or not config.getoption('--ff'):
        return

    for file_name in os.listdir(os.path.abspath('.cache/v/cache/')):
        if file_name != 'lastfailed':
            file_path = os.path.abspath('.cache/v/cache/%s' % file_name)
            if time.time() - os.path.getmtime(file_path) > 604800:  # 604800 seconds -> 7 days
                os.remove(file_path)

    serial_number = config.getoption('--sn')
    cache_path = os.path.abspath('.cache/v/cache/%s' % serial_number)
    if os.path.isfile(cache_path):
        # Found the name of test failed
        cache_file = open(cache_path, 'r')
        file_read = cache_file.read()

        sequence_name = file_read.split('\n', 1)[0]
        if config.getoption('--seq-config') != sequence_name:
            return

        item_fail_name = file_read.split('::')[1].split('"')[0]
        if '[' in item_fail_name:
            test_failed, option = item_fail_name.split('[', 1)
            option = option.split('-')[0].split(']')[0]
            if global_var['config'].exist('%s_0' % test_failed):
                # First option is not uut
                item_fail_name = '%s[%s' % (test_failed, option)
                test_failed = '%s_%s' % (test_failed, option)
            else:
                item_fail_name = test_failed

            # Verify loop option
            if global_var['config'].loop_infos() is not None:
                test_order_loop_start = global_var['config'].file_config[
                    global_var['config'].loop_infos()[0][0]]["test_order"]
                test_order_loop_stop = global_var['config'].file_config[
                    global_var['config'].loop_infos()[0][1]]["test_order"]
                # If test fail in loop, restart the loop
                if not global_var['config'].exist(test_failed) or \
                    (test_order_loop_start <=
                     global_var['config'].file_config[test_failed]['test_order'] <=
                     test_order_loop_stop):
                    test_failed = global_var['config'].loop_infos()[0][0]
                    test_failed, option = test_failed.rsplit('_', 1)
                    if global_var['config'].exist('%s_%s' % (test_failed, option)) and \
                            global_var['config'].exist('%s_0' % test_failed):
                        # First option is not uut
                        option = option.split(']', 1)[0].split('-')[0]
                        item_fail_name = '%s[%s' % (test_failed, option)
                        test_failed = '%s_%s' % (test_failed, option)
                    else:
                        item_fail_name = '%s_%s' % (test_failed, option)
        else:
            test_failed = item_fail_name

        # Verify if one test is required
        try:
            test_required = global_var['config'].file_config[test_failed]['test_required']
            if test_required is not None:
                # Found item_fail_name
                item_fail_name = test_required
        except KeyError:
            pass

        # Authorize all tests after found the first test failed
        first_test_failed_found = False
        items_temp = []
        for item in items:
            if first_test_failed_found:
                items_temp.append(item)
            elif item_fail_name in str(item):
                if '[' not in str(item_fail_name) or \
                        str(item).split(item_fail_name)[1][0] in [']', '-']:
                    first_test_failed_found = True
                    items_temp.append(item)
        items[:] = items_temp


def postfail_feature_management(test, item, skip, loop):
    """
    Manage the postfail feature according to the config test file
    """
    test_name, item_args = item_name_analyze(test)
    if global_var['config'].exist(test_name + "_0"):
        test_name = '%s_%s' % (test_name, item_args[0])

    post_fail = global_var['config'].post_fail(test_name)
    if post_fail is not None:
        if global_var['config'].post_fail(test_name) == "next_step":
            pass

        elif "test" in post_fail or "action" in post_fail:
            skip_reason = ""
            for test in item.session.items:
                item_name = test.name.split("[")[0]
                if global_var['config'].exist(item_name + "_0"):
                    item_name = item_name + "_" + test.name.split("[")[1][0]
                if post_fail in item_name:
                    break
                if test_name != item_name and skip is True:
                    test.add_marker(pytest.mark.skipif(
                        skip, reason=skip_reason))
    else:
        skip_reason = ""
        for each in item.session.items:
            item_name, item_args = item_name_analyze(each.name)
            if global_var['config'].exist(item_name + "_0"):
                item_name = '%s_%s' % (item_name, item_args[0])

            if global_var['config'].order(
                    item_name) != global_var['config'].order(test_name) and skip is True:
                if item_name != test_name:
                    each.add_marker(pytest.mark.skipif(
                        skip, reason=skip_reason))
            if item_name == test_name:
                if len(each.name.split("[")) > 1 and len(test.split("[")) > 1:
                    if each.name.split("[")[1] != test.split("[")[1] and loop:
                        each.add_marker(pytest.mark.skipif(
                            skip, reason=skip_reason))
