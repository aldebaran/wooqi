# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
General plugin file
"""
import pytest
from wooqi.src.plugin_fixtures import *
from wooqi.src.pytest_hooks import *
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
        if global_var['config'].exist(test[0] + "_" + test[1].replace("]", "").split('-')[0]):
            test_name = test_name + "_" + test[1].replace("]", "").split('-')[0]
        elif not global_var['config'].exist(test_name):
            cpt = 0
            while global_var['config'].exist('%s_%d' % (test[0], cpt)):
                cpt = cpt + 1
            num = int(test[1].replace("]", "").split('-')[0]) % cpt
            test_name = test[0] + "_" + str(num)
    return test_name


@pytest.fixture()
def test_info(request, logger, test_name):
    """
    Return current test info
    """
    logger.debug("Get " + str(request.node).split("'")[1] + " infos")
    uut = None
    uut2 = None
    var = None
    test_dico = {}
    test = str(request.node).split("'")[1].split("[")
    uuts = global_var['config'].uut(test_name)
    uuts2 = global_var['config'].uut2(test_name)
    if len(test) > 1:
        unit = test[1].replace("]", "")
        if uuts != None:
            for each in uuts:
                if each in unit:
                    var = each
            try:
                uut = int(var)
            except:
                uut = var
            test_dico["uuts"] = uuts
        if uuts2 != None:
            for each in uuts2:
                if each in unit:
                    var = each
            try:
                uut2 = int(var)
            except:
                uut2 = var

            test_dico["uuts2"] = uuts2
    elif uuts != None:
        test_dico["uuts"] = uuts

    params = ["time_test", "limit", "comparator", "misc_data", "nb_cycles"]
    for param in global_var['config'].file_config[test_name]:
        if param in params:
            info = getattr(global_var['config'], param)(test_name, uut, uut2)
            if info != None:
                test_dico[param] = info
        elif param != "uut" and param != "uut2":
            test_dico[param] = global_var['config'].file_config[test_name][param]
    logger.debug(test_dico)
    return test_dico
