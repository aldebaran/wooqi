# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Logger module
"""
import os
import sys
import logging
import logging.handlers
from ConfigParser import RawConfigParser, NoOptionError, NoSectionError
from wooqi.src import logger_gv


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


def init_logger(filename, directory, console_logger=True, maxSize=10000000):
    """init logging system"""

    CONFIG_FILE = 'logger.cfg'
    try:
        # if not all paramiko logs will be in test log
        logging.getLogger("paramiko").setLevel(logging.WARNING)
        # configuration
        parser = RawConfigParser()
        # do not convert attribute names to lower case
        parser.optionxform = lambda option: option
        config_file = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                   CONFIG_FILE))
        parser.read(config_file)
        file = get_option(parser, 'logging', 'file', True, evaluate=True)
        # directory = get_option(parser, 'logging', 'directory', 'logs')
        console_level = get_option(parser, 'logging', 'console_level', 'INFO')
        console_formatter_string = get_option(parser, 'logging',
                                              'console_formatter', '%(message)s')
        if file:
            file_level = get_option(parser, 'logging', 'file_level', 'WARNING')
            file_formatter_string = get_option(parser, 'logging', 'file_formatter',
                                               '%(asctime)s - %(levelname)s - %(message)s')

        # console logger
        if console_logger:
            # if invalid level in config file, set it to info
            if hasattr(logging, console_level):
                level = getattr(logging, console_level)
            else:
                level = logging.INFO

            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(logging.Formatter(console_formatter_string))
            filter = SingleLevelFilter(level)
            handler.addFilter(filter)
            logger_gv.addHandler(handler)

        # file logger
        if file:
            # if invalid level in config file, set it to info
            if hasattr(logging, file_level):
                level = getattr(logging, file_level)
            else:
                level = logging.INFO
            # create rotating file handler, add formatter to ch and add ch to logger
            handler = logging.handlers.RotatingFileHandler(os.path.join(directory, filename + '.log'),
                                                           maxBytes=maxSize, backupCount=5)
            handler.setFormatter(logging.Formatter(file_formatter_string))
            filter = SingleLevelFilter(level)
            handler.addFilter(filter)
            logger_gv.addHandler(handler)

        logger_gv.setLevel(logging.DEBUG)
        logger_gv.init = True
        return logger_gv
    except Exception, e:
        print e
