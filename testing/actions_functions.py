# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Actions
"""


def action_1(executed_tests, test_result):
    """
    action 1
    """
    executed_tests.append(1)
    assert test_result


def action_2(executed_tests, test_result):
    """
    action 2
    """
    executed_tests.append(2)
    assert test_result


def action_3(executed_tests, test_result):
    """
    action 3
    """
    executed_tests.append(3)
    assert test_result


def action_4(executed_tests, test_result):
    """
    action 4
    """
    executed_tests.append(4)
    assert test_result


def action_1_uut(executed_tests, test_result, uut):
    """
    action 1 with uut
    """
    executed_tests.append(1)
    assert test_result


def action_2_uut(executed_tests, test_result, uut):
    """
    action 2 with uut
    """
    executed_tests.append(2)
    assert test_result


def action_1_uut2(executed_tests, test_result, uut, uut2):
    """
    action 1 with two uut
    """
    executed_tests.append(1)
    assert test_result


def action_2_uut2(executed_tests, test_result, uut, uut2):
    """
    action 2 with two uut
    """
    executed_tests.append(2)
    assert test_result


def action_loop_fail_second_call(executed_tests, test_result):
    """
    loop test fail on second call
    """
    executed_tests.append(0)
    assert executed_tests.count(0) == 1
