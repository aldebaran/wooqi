# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
pip package setup
"""

from setuptools import setup, find_packages
from wooqi import __version__

# For development purposes, install it with pip install -user -e
# or python setup.py develop


def get_long_description():
    """Return readme description"""
    with open('README.md') as fp:
        return fp.read()


import os
import sys
import setuptools
import pkg_resources
from setuptools import setup, Command

classifiers = [
    'Development Status :: 6 - Mature',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS :: MacOS X',
    'Topic :: Software Development :: Testing',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
] + [
    ('Programming Language :: Python :: %s' % x)
    for x in '2 2.6 2.7 3 3.3 3.4 3.5 3.6'.split()

def has_environment_marker_support():
    """
    Tests that setuptools has support for PEP-426 environment marker support.

    The first known release to support it is 0.7 (and the earliest on PyPI seems to be 0.7.2
    so we're using that), see: http://pythonhosted.org/setuptools/history.html#id142

    References:

    #defining-conditional-dependencies
    * https://wheel.readthedocs.io/en/latest/index.html
    * https://www.python.org/dev/peps/pep-0426/#environment-markers
    """
    try:
        return pkg_resources.parse_version(setuptools.__version__) >= pkg_resources.parse_version('0.7.2')
    except Exception as exc:
        sys.stderr.write("Could not test setuptool's version: %s\n" % exc)
        return False


def main():
    # pluggy is vendored in _pytest.vendored_packages
<<<<<<< master
    install_requires= ['py>=1.4.33', 'setuptools']
    extras_require= {}
=======
    install_requires = ['py>=1.4.33', 'setuptools', 'mock>=1.0.1']
    extras_require = {}
>>>>>>> Add spec plugin source code
    if has_environment_marker_support():
        extras_require[':python_version=="2.6"']= ['argparse', 'ordereddict']
        extras_require[':sys_platform=="win32"']= ['colorama']
    else:
        if sys.version_info < (2, 7):
            install_requires.append('argparse')
            install_requires.append('ordereddict')
        if sys.platform == 'win32':
            install_requires.append('colorama')

    setup(
        name="wooqi",
        version=__version__,
        description="Pytest plugin allowing to parametrize all the test sequence thanks to a config file",
        # packages=find_packages(),
        license='BSD-3',
        long_description=get_long_description(),
        long_description_content_type='text/markdown',
        url="https://github.com/aldebaran/wooqi",
        download_url="https://pypi.org/project/wooqi/",
        entry_points={'console_scripts': [
            'wooqi = wooqi.__main__:main', 'prout=wooqi.pytest.pytest:main'], 'pytest11': ['wooqi = wooqi.plugin_wooqi']},
        # include_package_data=True,
        # name='pytest',
        # description='pytest: simple powerful testing with Python',
        # long_description=long_description,
        # use_scm_version={
        #     'write_to': '_pytest/_version.py',
        # },
        # url='http://pytest.org',
        # license='MIT license',
        platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
        # entry_points={'console_scripts':
        #               ['pytest=pytest:main', 'py.test=pytest:main']},
        # classifiers=classifiers,
        # keywords="test unittest",
        cmdclass={'test': PyTest},
        # the following should be enabled for release
        setup_requires=['setuptools-scm'],
        install_requires=install_requires,
        extras_require=extras_require,
        packages=['wooqi.pytest._pytest', 'wooqi.pytest._pytest.assertion',
                  'wooqi.pytest._pytest._code', 'wooqi.pytest._pytest.vendored_packages'],
        py_modules=['wooqi_pytest'],
        zip_safe=False,
    )


class PyTest(Command):
    user_options= []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        PPATH= [x for x in os.environ.get('PYTHONPATH', '').split(':') if x]
        PPATH.insert(0, os.getcwd())
        os.environ['PYTHONPATH']= ':'.join(PPATH)
        errno= subprocess.call(
            [sys.executable, 'wooqi_pytest.py', '--ignore=doc'])
        raise SystemExit(errno)


if __name__ == '__main__':
    main()
