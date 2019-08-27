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
from itertools import product
from wooqi.src import global_var


def get_uuts(test_name):
    """
    Return uut and uut2 according to test
    """
    uut = []
    uut2 = []
    if 'uut' in global_var['config'].file_config[test_name]:
        uut = global_var['config'].uut(test_name)
    if 'uut2' in global_var['config'].file_config[test_name]:
        uut2 = global_var['config'].uut2(test_name)
    return uut, uut2


def item_loop_option_analyse(item, test_name, first_arg):
    """
    Return config test name and the iteration number according to loop option
    """
    if "loop" in item.keywords.__dict__["_markers"].keys():
        # Test defined one time in config file
        if global_var['config'].exist(test_name):
            iter_number = int(first_arg)
        # Test defined multiple time in config file and is the first iteration
        elif global_var['config'].exist('{}_{}'.format(test_name, first_arg)):
            iter_number = 0
            test_name = '{}_{}'.format(test_name, first_arg)
        # Test defined multiple time in config file but not is the first iteration
        else:
            loop_tests = global_var['config'].loop_infos()[0]
            cpt = 0
            nb_test_in_loop = 0
            first_test_in_loop = None
            # Count the number of test defined in config file
            while global_var['config'].exist('{}_{}'.format(test_name, cpt)):
                test_order = global_var[
                    'config'].file_config['{}_{}'.format(test_name, cpt)]['test_order']
                first_loop_test_order = global_var[
                    'config'].file_config[loop_tests[0]]["test_order"]
                last_loop_test_order = global_var[
                    'config'].file_config[loop_tests[1]]["test_order"]
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
            test_name = '{}_{}'.format(test_name, call_number)
    else:
        iter_number = 0
        # If test_name exist first_arg is uut
        if not global_var['config'].exist(test_name):
            test_name = '{}_{}'.format(test_name, first_arg)
    return test_name, iter_number


def filter_order_tests(config, items):
    """
    Filter and re-order the tests according to the config test file
    """
    pytest_tests = {}
    file_config = global_var['config'].file_config
    for session in file_config:
        if session.startswith('test_') or session.startswith('action_'):
            if session == 'test_info':
                continue

            if 'test_info' in file_config and 'loop_iter' in file_config['test_info']:
                if 'wooqi_loop_iter' not in file_config[session]:
                    loop_tests, iter_number = global_var['config'].loop_infos()
                    loop_test_start = global_var['config'].loop_infos()[0][0]
                    iter_number = file_config[loop_test_start]['test_order']
                    # All tests before the loop start use the first iteration number
                    if file_config[session]['test_order'] < iter_number:
                        iter_number = 0
                    # All tests after loop option use the last iteration number
                    else:
                        iter_number = global_var['config'].loop_infos()[1] - 1
                # Else: For tests in the loop, the iter_number is defined after
            else:
                # Without loop option, all tests are the same iter_number level
                iter_number = 0

            if len(session.split('-')) == 0:
                test_name = session
            else:
                test_name = session.replace('-', '[')

            if 'wooqi_loop_iter' in file_config[session]:
                loop_iter = file_config[session]['wooqi_loop_iter']
                loop_iter = range(loop_iter)
            else:
                loop_iter = []

            uut, uut2 = get_uuts(session)

            if uut2:
                if loop_iter:
                    list_param = list(product(loop_iter, uut, uut2))
                else:
                    list_param = list(product(uut, uut2))
            elif uut:
                if loop_iter:
                    list_param = list(product(loop_iter, uut))
                else:
                    list_param = uut
            elif loop_iter:
                list_param = loop_iter
            else:
                list_param = []

            test_order = file_config[session]['test_order']
            if list_param:
                if '[' not in test_name:
                    test_name = '{}['.format(test_name)
                for params in list_param:
                    if type(params) is tuple:
                        concatenate_params = ''
                        for param in params:
                            concatenate_params += '{}-'.format(param)
                        concatenate_params = concatenate_params[:-1]
                    else:
                        concatenate_params = params
                    test_name_with_param = '{}-{}]'.format(
                        test_name, concatenate_params).replace('[-', '[')

                    if loop_iter:
                        if type(params) is tuple:
                            iter_number = params[0]
                        else:
                            iter_number = params
                        pytest_tests[test_name_with_param] = {'session': session,
                                                              'test_order': test_order,
                                                              'iter_number': iter_number}
                    else:
                        pytest_tests[test_name_with_param] = {'session': session,
                                                              'test_order': test_order,
                                                              'iter_number': iter_number}
            else:
                if '[' in test_name:
                    test_name += ']'
                pytest_tests[test_name] = {'session': session,
                                           'test_order': test_order,
                                           'iter_number': iter_number}

    # Link test_name with the function
    for item in items:
        if item.name in pytest_tests:
            pytest_tests[item.name]['item'] = item

            session_name = pytest_tests[item.name]['session']
            # To manage reruns option
            if 'reruns' in file_config[session_name]:
                pytest_tests[item.name]['item'].keywords.__dict__["reruns"] = 0
                pytest_tests[item.name]['item'].add_marker(
                        pytest.mark.flaky(reruns=global_var['config'].reruns(session_name)))
            # To manage timeout option
            if 'timeout' in file_config[session_name]:
                pytest_tests[item.name]['item'].add_marker(
                        pytest.mark.timeout(global_var['config'].timeout(session_name)))

    # Check if all action/test defined in the configuration file exist
    for test_name in pytest_tests:
        if 'item' not in pytest_tests[test_name]:
            msg = '{} not found, ' \
                'please verify the test definition and your configuration file'.format(test_name)
            print(msg)
            raise Exception(msg)

    # Create an ordered list
    ordered_list = sorted(pytest_tests, key=lambda k: (
            pytest_tests[k]['iter_number'], pytest_tests[k]['test_order'], k))
    items_temp = []
    for test_name in ordered_list:
        items_temp.append(pytest_tests[test_name]['item'])
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
            file_path = os.path.abspath('.cache/v/cache/{}'.format(file_name))
            if time.time() - os.path.getmtime(file_path) > 604800:  # 604800 seconds -> 7 days
                os.remove(file_path)

    serial_number = config.getoption('--sn')
    cache_path = os.path.abspath('.cache/v/cache/{}'.format(serial_number))
    if os.path.isfile(cache_path):
        # Found the name of test failed
        with open(cache_path, 'r') as f:
            file_read = f.read()

        sequence_name = file_read.split('\n', 1)[0]
        if config.getoption('--seq-config') != sequence_name:
            return

        item_fail_name = file_read.split('::')[1].split('"')[0]
        if '[' not in item_fail_name:
            test_failed = item_fail_name
        else:
            test_failed, option = item_fail_name.split('[', 1)
            option = option.split('-')[0].split(']')[0]

            if '{}-{}'.format(test_failed, option) in global_var['config'].file_config:
                item_fail_name = '{}-{}'.format(test_failed, option)
                test_failed = '{}[{}-'.format(test_failed, option)
            else:
                item_fail_name = test_failed.split('[')[0]

            # Verify loop option
            if 'wooqi_loop_iter' in global_var['config'].file_config[item_fail_name]:
                item_fail_name = global_var['config'].loop_infos()[0][0]

                test_failed = '{}'.format(item_fail_name.split('-')[0])
                if '-' in item_fail_name:
                    test_failed = '{}[{}-'.format(test_failed, item_fail_name.split('-')[1])

        # Verify if one test is required
        if 'test_required' in global_var['config'].file_config[item_fail_name]:
            # Found item_fail_name
            item_fail_name = global_var['config'].file_config[item_fail_name]['test_required']

            test_failed = '{}'.format(item_fail_name.split('-')[0])
            if '-' in item_fail_name:
                test_failed = '{}[{}-'.format(test_failed, item_fail_name.split('-')[1])

        # Authorize all tests after found the first test failed
        first_test_failed_found = False
        items_temp = []
        for item in items:
            if first_test_failed_found:
                items_temp.append(item)
            elif test_failed in item.name or (
                    test_failed.endswith('-') and '{}]'.format(test_failed[:-1]) == item.name):
                first_test_failed_found = True
                items_temp.append(item)
        items[:] = items_temp


def postfail_feature_management(item, skip):
    """
    Manage the postfail feature according to the config test file
    """
    if not skip:
        return

    skip_reason = ""
    file_config = global_var['config'].file_config

    # test_name according in file_config
    test_name = item.name.split('[')[0]
    if test_name not in file_config:
        call_number = item.name.split('[')[1].split('-')[0].replace(']', '')
        base_name = '{}[{}-'.format(test_name, call_number)
        test_name = '{}-{}'.format(test_name, call_number)
    else:
        base_name = '{}['.format(test_name)  # base_name is the item name without parameters

    if 'wooqi_loop_iter' in file_config[test_name]:
        base_name += item.name.replace(base_name, '').split('-')[0].replace(']', '')

    post_fail = global_var['config'].post_fail(test_name)
    if post_fail is not None:
        if post_fail.lower() == "next_step":
            return
        else:
            if '-' in post_fail:
                # Adapt post_fail to item.name format
                post_fail = '{}[{}]'.format(post_fail.split('-')[0], post_fail.split('-')[1])

    for session_item in item.session.items:
        if post_fail and (post_fail == session_item.name or
                          post_fail.replace(']', '-') in session_item.name):
            break
        elif base_name in session_item.name:
            continue
        else:
            session_item.add_marker(pytest.mark.skipif(skip, reason=skip_reason))
