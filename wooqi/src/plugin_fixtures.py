# -*- coding: utf-8 -*-
"""
Wooqi fixtures
"""
import os
import time
import ConfigParser
import pytest
from wooqi.src.logger import init_logger
from wooqi.src import global_var


def read_cfg(cfg_file):
    """
    Read config file
    """
    cfg = ConfigParser.ConfigParser()
    cfg.read(cfg_file)
    return cfg


def current_time():
    """
    get the current date & time
    """
    current_time = time.strftime('%y_%m_%d_%H-%M-%S')
    return current_time


@pytest.fixture(scope="session")
def test_config_parser(test_config):
    """
    Get parser of the test config file
    """
    if global_var['config'] != None:
        return read_cfg(test_config)
    else:
        return None


@pytest.fixture(scope="session")
def test_time():
    """
    return current time
    """
    return current_time()


@pytest.fixture(scope="session")
def log_folder(serial_number):
    """
    return the path of the log folder
    """
    os.getcwd()
    if global_var['config'] != None:
        list_dir = os.listdir(os.getcwd())
        if "reports" not in list_dir:
            os.makedirs(os.getcwd() + "/reports/")
        if serial_number not in os.listdir(os.getcwd() + "/reports/"):
            os.makedirs(os.getcwd() + "/reports/" + serial_number + "/")
        folder_path = os.getcwd() + "/reports/" + serial_number + "/"
        return folder_path
    else:
        return None


@pytest.fixture(scope="session")
def log_name(serial_number, test_time, test_config):
    """
    return the name of the log file
    """
    if global_var['config'] != None:
        test = os.path.basename(test_config).replace(".ini", "")
        name = serial_number + '_' + test + '_' + test_time
        return name
    else:
        return None


@pytest.fixture(scope="session", autouse=True)
def logger(log_name, log_folder, request):
    """
    Return logger object to create .log file
    """
    # -s option is a shortcut for --capture=no
    if global_var['config'] != None:
        console_logger = True if request.config.getoption('--capture') == 'no' else False
        logger = init_logger(log_name, log_folder, console_logger)
        logger.debug('=====================================================')
        logger.debug('================ BEGINNING OF SCRIPT ================')
        logger.debug('=====================================================')
        return logger
    else:
        return None
