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
    print "***************************************"
    print "***** Initiliazing Wooqi project ******"
    print "***************************************"
    print ""
    if not len(args) > 1:
        print "[ERROR] usage: wooqi --init-project my_project_name"
    else:
        project_name = args[1]
        print ">>> Create a new project '" + project_name + "' in '" + os.path.abspath(".") +"' ? (y/n)"
        answer = raw_input()
        if answer == 'y':
            print ">>> Creating project..."
            project_path = os.path.abspath(project_name)
            if not os.path.isdir(project_path):
                try:
                    project_template_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               "project_template"))
                    # ignore files with '.pyc' extension and ignore '__pycache__' directory
                    ignore_func = lambda d, files: [f for f in files if (os.path.isfile(os.path.join(d, f)) and
                                                    f[-4:] == '.pyc') or f == '__pycache__']
                    shutil.copytree(project_template_path, project_path, ignore=ignore_func)
                except OSError as e:
                    print('Directory not copied. Error: %s' % e)
                print ">>> Project initialization complete."
            else:
                print ">>> Directory " + project_name + " already exists"
                print ">>> Project initialization failed."


def main(args=None):
    """
    Main
    """
    if args is None:
        args = sys.argv[1:]
    arguments = ""
    if "--version" in args:
        print "Wooqi " + __version__
    elif "--init-project" in args:
        init_command(args[args.index('--init-project'):])
    elif "--seq-config" in args:
        arguments = " ".join(args)
        print "*********************************"
        print "***** Wooqi tests sequencer *****"
        print "*********************************"
        exit_code = os.system("py.test " + arguments + " --spec --wooqi")
        return exit_code >> 8
    else:
        print "Usage: "
        print "* Launch a test sequence:"
        print "    wooqi --seq-config TEST_SEQUENCE_FILE --sn SAMPLE_NAME/SERIAL_NUMBER [-s] [-k TEST_NAME] [--lf]"
        print "* Initialize a wooqi project:"
        print "    wooqi --init-project my_project"

if __name__ == '__main__':
    sys.exit(main())
