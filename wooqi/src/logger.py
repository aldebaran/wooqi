# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Logger module
"""
import logging.handlers
from ConfigParser import NoOptionError, NoSectionError


class SingleLevelFilter(logging.Filter):
    # cf: http://stackoverflow.com/questions/1383254/logging-streamhandler-and-standard-streams

    def __init__(self, passlevel):
        self.passlevel = passlevel

    def filter(self, record):
        return record.levelno >= self.passlevel


def get_option(parser, section, option, default_value=None, evaluate=False):
    """Reads an option in a config file. The default value is used if the
    option does not exist"""
    try:
        option_value = parser.get(section, option)
        if evaluate:
            option_value = eval(option_value)
        return option_value
    except (NoOptionError, NoSectionError):
        return default_value
