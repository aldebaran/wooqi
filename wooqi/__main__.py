"""
wooqi entry point
"""

import sys
import os
from wooqi import __version__


def main(args=None):
    """
    Main
    """
    if args is None:
        args = sys.argv[1:]
    arguments = ""
    if "--version" in args:
        print "Wooqi " + __version__
    elif "--seq-config" in args:
        for each in args:
            arguments = arguments + " " + each
        print "*********************************"
        print "***** Wooqi tests sequencer *****"
        print "*********************************"
        os.system("py.test" + arguments + " --spec --wooqi")
    else:
        print "usage: wooqi --seq-config TEST_SEQUENCE_FILE --sn SAMPLE_NAME/SERIAL_NUMBER [-s] [-k TEST_NAME] [--lf]"

if __name__ == '__main__':
    sys.exit(main())
