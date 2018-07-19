# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Pytest sequencer tests conftest
"""
import pytest


@pytest.fixture(scope="session")
def executed_tests(request, test_config_parser, logger):
    """
    Analyze executed tests
    """
    executed_tests = []

    def analyze_result():
        """
        Analyze list
        """
        required_list = []
        required_list = [int(x) for x in test_config_parser.get(
            "Result", mode_tests).split(",")]
        test_name = test_config_parser.get("Result", "test_name")
        fail_message = test_name + " failed"
        logger.info(test_name)
        logger.info("Executed tests = " + str(executed_tests))
        logger.info("Required test = " + str(required_list))
        assert executed_tests == required_list, fail_message
        logger.info("TEST PASSED")

    if request.config.getoption("--ff"):
        mode_tests = 'rerun_tests'
    else:
        mode_tests = 'executed_tests'
    request.addfinalizer(analyze_result)
    return executed_tests


@pytest.fixture(scope="function")
def test_result(test_info):
    """
    Test result
    """
    if "result" not in test_info.keys():
        return True
    elif test_info["result"].lower() == "pass":
        return True
    elif test_info["result"].lower() == "fail":
        return False
    else:
        error = "Bad parameter in test config file"
        pytest.fail(error)


@pytest.fixture()
def fixture_setup_fail(executed_tests, test_result):
    """
    Fixture setup fail
    """
    error = "Fixture setup fail"
    pytest.fail(error)


@pytest.fixture()
def fixture_teardown_fail(request):
    """
    Fixture teardown fail
    """
    def end():
        error = "Fixture teardown fail"
        pytest.fail(error)
    request.addfinalizer(end)
