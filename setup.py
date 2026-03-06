# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""pip package setup"""

from setuptools import find_packages, setup

from wooqi import __version__

# For development purposes, install it with pip install -user -e
# or python setup.py develop


def get_long_description():
    """Return readme description"""
    with open("README.md") as fp:
        return fp.read()


setup(
    version=__version__,
    name="wooqi",
    description="Pytest plugin allowing to parametrize all the test sequence thanks to a config file",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="BSD-3",
    url="https://github.com/aldebaran/wooqi",
    download_url="https://pypi.org/project/wooqi/",
    entry_points={
        "pytest11": ["wooqi = wooqi.plugin"],
        "console_scripts": ["wooqi = wooqi.__main__:main"],
    },
    include_package_data=True,
    install_requires=[
        "pytest>=7.0",
        "pytest-rerunfailures>=13.0",
        "pytest-timeout>=2.0",
        "pytest-spec>=3.0",
        "configparser",
    ],
    setup_requires=["pytest-runner"],
    test_require=["pytest"],
)
