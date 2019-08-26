# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
wooqi entry point
"""

import sys
import os
import shutil
from wooqi import __version__


def init_command(args):
    """
    Manage the `wooqi init` command
    """
    print("***************************************")
    print("***** Initiliazing Wooqi project ******")
    print("***************************************\n")
    if not len(args) > 1:
        print("[ERROR] usage: wooqi --init-project my_project_name")
    else:
        project_name = args[1]
        print(">>> Create a new project '{}' in '{}' ? (y/n)".format(
            project_name, os.path.abspath(".")))
        answer = raw_input()
        if answer == 'y':
            print(">>> Creating project...")
            project_path = os.path.abspath(project_name)
            if not os.path.isdir(project_path):
                try:
                    project_template_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                                         "project_template"))

                    # ignore files with '.pyc' extension and ignore '__pycache__' directory
                    def ignore_func(d, files):
                        return [f for f in files if f == '__pycache__' or f.endswith('.pyc')]

                    shutil.copytree(project_template_path, project_path, ignore=ignore_func)
                except OSError as e:
                    print("Directory not copied. Error: {}".format(e))
                print(">>> Project initialization complete.")
            else:
                print(">>> Directory {} already exists".format(project_name))
                print(">>> Project initialization failed.")


def print_usage():
    """
    Print the usage of the Wooqi command
    """
    usage_txt = """
*********************************
***** Wooqi tests sequencer *****
*********************************

--- Independant commands -------------------------------------------------------
    wooqi [args]
        --init-project XXXX     Initialize a Wooqi project named XXXX,
                                creating all necessary directories and files.
        -v/--version            Print the installed version of Wooqi
        -h/--help               Display this help

--- Command to launch tests -------------------------------------------------------
    wooqi [args]
        --seq-config XXXX       (required) relative path to the .ini file of the test sequence
        --sn XXXX               (required) Specific SAMPLE_NAME or SERIAL_NUMBER.
                                Used to name the logs.
        -s                      Display logs and print output in the console.
        -k XXXX                 Execute the specified tests only (name can be incomplete)
        --lf                    Execute the last failed test only.

    Examples:
        * Launch a test sequence:
            wooqi --seq-config sequences/test_motors.ini --sn MySample -s"
        * Initialize a wooqi project:
            wooqi --init-project my_project"
"""
    print(usage_txt)


def main(args=None):
    """
    Main
    """
    if args is None:
        args = sys.argv[1:]
    arguments = ""
    if "--help" in args or "-h" in args:
        print_usage()
    elif "--version" in args or "-v" in args:
        print(__version__)
    elif "--init-project" in args:
        init_command(args[args.index('--init-project'):])
    elif "--seq-config" in args:
        if "--ff" not in args and "--lf" not in args:
            args.append("--cache-clear")
        arguments = " ".join(args)
        print("*********************************")
        print("***** Wooqi tests sequencer *****")
        print("*********************************")
        # On Unix, the return value is a 16-bit number that contains
        # two different pieces of information. From the documentation:
        # low byte is the signal number that killed the process
        # high byte is the exit status (if the signal number is zero)
        val = os.system("py.test {} --spec --wooqi".format(arguments))
        if val & 0xF > 0:
            val = val + 255
        exit(val >> 8)
    else:
        print("Error: unknown Wooqi command ! Please see usage below.")
        print_usage()
        exit(-1)


if __name__ == '__main__':
    sys.exit(main())
