# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Tests
"""


def test_1(executed_tests, test_result):
    """
    test 1
    """
    executed_tests.append(1)
    assert test_result


def test_2(executed_tests, test_result):
    """
    test 2
    """
    executed_tests.append(2)
    assert test_result


def test_3(executed_tests, test_result):
    """
    test 3
    """
    executed_tests.append(3)
    assert test_result


def test_4(executed_tests, test_result):
    """
    test 4
    """
    executed_tests.append(4)
    assert test_result


def test_1_uut(executed_tests, test_result, uut):
    """
    test 1 with uut
    """
    executed_tests.append(1)
    assert test_result


def test_2_uut(executed_tests, test_result, uut):
    """
    test 2 with uut
    """
    executed_tests.append(2)
    assert test_result


def test_1_uut2(executed_tests, test_result, uut, uut2):
    """
    test 1 with two uut
    """
    executed_tests.append(1)
    assert test_result


def test_2_uut2(executed_tests, test_result, uut, uut2):
    """
    test 2 with two uut
    """
    executed_tests.append(2)
    assert test_result


def test_loop_fail_second_call(executed_tests, test_result):
    """
    loop test fail on second call
    """
    executed_tests.append(0)
    assert executed_tests.count(0) == 1


def test_setup_fixture(fixture_setup_fail):
    """
    test setup fixture fail
    """
    pass


def test_teardown_fixture(fixture_teardown_fail):
    """
    test teardown fixture fail
    """
    pass
