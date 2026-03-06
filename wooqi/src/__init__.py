# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Define plugin global variable
"""

import logging

import pytest

global_var = {}
WOOQI_RERUNS_KEY = pytest.StashKey[int]()
logger = logging.getLogger(__package__)
