# -*- coding: utf-8 -*-
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
        "--seq_config",
        default=None,
        action="store",
        help="Test file config"
    )
    group.addoption(
        "--sn",
        action="store",
        default="test",
        help="Robot serial number"
    )


@pytest.fixture(scope="session")
def test_config(request):
    """
    Test config
    """
    return request.config.getoption("--seq_config")


@pytest.fixture(scope="session")
def serial_number(request):
    """
    Serial number
    """
    return request.config.getoption("--sn")


@pytest.fixture()
def test_info(request):
    """
    Return current test info
    """
    uut = None
    uut2 = None
    var = None
    test_dico = {}
    test = str(request.node).split("'")[1].split("[")
    test_name = test[0]
    if len(test) > 1:
        if global_var['config'].exist(test[0] + "_" + test[1][0]):
            test_name = test_name + "_" + test[1][0]

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
                uut = None
            except:
                uut = var
            test_dico["uuts"] = uuts
        if uuts2 != None:
            for each in uuts2:
                if each in unit:
                    var = each
            try:
                uut2 = int(var)
                uut2 = None
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
    return test_dico
