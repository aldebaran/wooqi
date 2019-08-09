# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
General plugin file
"""
import pytest
from wooqi.src.plugin_fixtures import test_config_parser, test_sequence_name, test_time
from wooqi.src.plugin_fixtures import wooqi_conf, log_folder, log_name, logger
from wooqi.src.pytest_hooks import pytest_collection_modifyitems, pytest_runtest_makereport
from wooqi.src.pytest_hooks import pytest_report_header, pytest_generate_tests
from wooqi.src.pytest_hooks import pytest_sessionfinish, pytest_unconfigure
from wooqi.src import global_var


def pytest_addoption(parser):
    """
    Configuration of pytest parsing
    """
    group = parser.getgroup('general')
    group.addoption(
        "--seq-config",
        default=None,
        action="store",
        help="Test file config"
    )
    group.addoption(
        "--sn",
        action="store",
        default="test",
        help="Sample serial number or name"
    )
    group.addoption(
        "--wooqi",
        action="store_true",
        dest='wooqi tag',
        help="wooqi tag to check if the test is runned thanks to wooqi"
    )


@pytest.fixture(scope="session")
def test_config(request, wooqi):
    """
    Test config
    """
    return request.config.getoption("--seq-config")


@pytest.fixture(scope="session")
def serial_number(request, wooqi):
    """
    Serial number
    """
    return request.config.getoption("--sn")


@pytest.fixture(scope="session")
def wooqi(request):
    """
    Check if the test is runned with wooqi
    """
    return request.config.getoption("--wooqi")


@pytest.fixture()
def test_name(request, logger):
    """
    Return current test name
    """
    test = str(request.node).split("'")[1].split("[")
    test_name = test[0]
    if len(test) > 1:
        if global_var['config'].exist('{}_{}'.format(
                test[0], test[1].replace("]", "").split('-')[0])):
            test_name = '{}_{}'.format(test_name, test[1].replace("]", "").split('-')[0])
        elif not global_var['config'].exist(test_name):
            cpt = 0
            while global_var['config'].exist('{}_{}'.format(test[0], cpt)):
                cpt = cpt + 1
            num = int(test[1].replace("]", "").split('-')[0]) % cpt
            test_name = '{}_{}'.format(test[0], num)
    return test_name


@pytest.fixture()
def test_info(request, logger, test_name):
    """
    Return current test info
    """
    logger.debug("Get {} infos".format(str(request.node).split("'")[1]))
    uut = None
    uut2 = None
    var = None
    test_dico = {}
    test = str(request.node).split("'")[1].split("[")
    uuts = global_var['config'].uut(test_name)
    uuts2 = global_var['config'].uut2(test_name)
    if len(test) > 1:
        unit = test[1].replace("]", "")
        if uuts is not None:
            for each in uuts:
                if each in unit:
                    var = each
            try:
                uut = int(var)
            except Exception:
                uut = var
            test_dico["uuts"] = uuts
        if uuts2 is not None:
            for each in uuts2:
                if each in unit:
                    var = each
            try:
                uut2 = int(var)
            except Exception:
                uut2 = var

            test_dico["uuts2"] = uuts2
    elif uuts is not None:
        test_dico["uuts"] = uuts

    params = ["time_test", "limit", "comparator", "misc_data", "nb_cycles"]
    for param in global_var['config'].file_config[test_name]:
        if param in params:
            info = getattr(global_var['config'], param)(test_name, uut, uut2)
            if info is not None:
                test_dico[param] = info
        elif param != "uut" and param != "uut2":
            test_dico[param] = global_var['config'].file_config[test_name][param]
    logger.debug(test_dico)
    return test_dico
