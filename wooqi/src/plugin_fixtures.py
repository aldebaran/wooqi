# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

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
def test_sequence_name(test_config):
    """
    Return the name of the test according to the .ini file
    """
    if global_var['config'] != None:
        return os.path.basename(test_config).replace(".ini", "")
    else:
        return None


@pytest.fixture(scope="session")
def test_time():
    """
    return current time
    """
    return current_time()


@pytest.fixture(scope="session")
def wooqi_conf(request):
    """
    Wooqi configuration file read from specific project which is using wooqi
    Return a dictionary containing all configuration attributes
    """
    config_file_path = os.getcwd() + "/wooqi_conf.cfg"
    if os.path.isfile(config_file_path):
        config = read_cfg(config_file_path)
    else:
        config = None
    return config


@pytest.fixture(scope="session")
def log_folder(serial_number, wooqi_conf, test_time, test_sequence_name):
    """
    return the path of the log folder
    """
    current_dir = os.getcwd()
    # Get log configuration from the specific project which is using wooqi
    if wooqi_conf is not None:
        if wooqi_conf.has_option("LOGS", "LOGS_DIRECTORY"):
            # If no specific configuration, default report path is /reports/<SN>/
            log_conf = wooqi_conf.get("LOGS", "LOGS_DIRECTORY").split()
        else:
            log_conf = ["sn"]
    else:
        # If no specific configuration, default report path is /reports/<SN>/
        log_conf = ["sn"]

    if global_var['config'] != None:
        # All reports are in reports/ directory
        if not os.path.isdir(current_dir + "/reports"):
            os.makedirs(current_dir + "/reports/")
        folder_path = current_dir + "/reports/"

        for item in log_conf:
            # Add serial number to log directory
            if item == "sn":
                if not os.path.isdir(folder_path + serial_number):
                    os.makedirs(folder_path + serial_number)
                folder_path += serial_number + "/"
            # Add date to log directory
            elif item == "date":
                if not os.path.isdir(folder_path + test_time):
                    os.makedirs(folder_path + test_time)
                folder_path += test_time + "/"
            # Add sequence file name to log directory
            elif item == "seq_name":
                if not os.path.isdir(folder_path + test_sequence_name):
                    os.makedirs(folder_path + test_sequence_name)
                folder_path += test_sequence_name + "/"
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
