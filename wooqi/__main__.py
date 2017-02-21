"""
wooqi entry point
"""

import sys
import os


def main(args=None):
    """
    Main
    """
    print "*********************************"
    print "***** Wooqi tests sequencer *****"
    print "*********************************"
    if args is None:
        args = sys.argv[1:]
    arguments = ""
    if "--seq-config" in args:
        for each in args:
            arguments = arguments + " " + each
        os.system("py.test" + arguments + " --spec --wooqi")
if __name__ == '__main__':
    sys.exit(main())
