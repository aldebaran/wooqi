"""
wooqi entry point
"""

import sys
import os


def main(args=None):
    """
    Main
    """
    print "haha"
    print args
    if args is None:
        args = sys.argv[1:]
    arguments = ""
    for each in args:
        arguments = arguments + " " + each
    print "py.test" + arguments
    os.system("py.test" + arguments)

if __name__ == '__main__':
    sys.exit(main())
