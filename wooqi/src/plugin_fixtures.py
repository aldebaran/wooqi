# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Wooqi fixtures
"""
import os
import time
from configparser import ConfigParser
import pytest
from wooqi.src import global_var


def read_cfg(cfg_file):
    """
    Read config file
    """
    cfg = ConfigParser(strict=False)
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
    if global_var['config'] is not None:
        return read_cfg(test_config)
    else:
        return None


@pytest.fixture(scope="session")
def test_sequence_name(test_config):
    """
    Return the name of the test according to the .ini file
    """
    if global_var['config'] is not None:
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
def wooqi_conf():
    """
    Wooqi configuration file read from specific project which is using wooqi
    Return a dictionary containing all configuration attributes
    """
    config_file_path = '{}/wooqi_conf.cfg'.format(os.getcwd())
    if os.path.isfile(config_file_path):
        config = read_cfg(config_file_path)
    else:
        config = None
    return config
