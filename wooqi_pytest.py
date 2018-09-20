# PYTHON_ARGCOMPLETE_OK
"""
pytest: unit and functional testing with Python.
"""


# else we are imported

from wooqi.pytest._pytest.config import (
    main, UsageError, _preloadplugins, cmdline,
    hookspec, hookimpl
)
from wooqi.pytest._pytest.fixtures import fixture, yield_fixture
from wooqi.pytest._pytest.assertion import register_assert_rewrite
from wooqi.pytest._pytest.freeze_support import freeze_includes
from wooqi.pytest._pytest import __version__
from wooqi.pytest._pytest.debugging import pytestPDB as __pytestPDB
from wooqi.pytest._pytest.recwarn import warns, deprecated_call
from wooqi.pytest._pytest.outcomes import fail, skip, importorskip, exit, xfail
from wooqi.pytest._pytest.mark import MARK_GEN as mark, param
from wooqi.pytest._pytest.main import Item, Collector, File, Session
from wooqi.pytest._pytest.fixtures import fillfixtures as _fillfuncargs
from wooqi.pytest._pytest.python import (
    Module, Class, Instance, Function, Generator,
)

from wooqi.pytest._pytest.python_api import approx, raises

set_trace = __pytestPDB.set_trace

__all__ = [
    'main',
    'UsageError',
    'cmdline',
    'hookspec',
    'hookimpl',
    '__version__',
    'register_assert_rewrite',
    'freeze_includes',
    'set_trace',
    'warns',
    'deprecated_call',
    'fixture',
    'yield_fixture',
    'fail',
    'skip',
    'xfail',
    'importorskip',
    'exit',
    'mark',
    'param',
    'approx',
    '_fillfuncargs',

    'Item',
    'File',
    'Collector',
    'Session',
    'Module',
    'Class',
    'Instance',
    'Function',
    'Generator',
    'raises',


]

if __name__ == '__main__':
    # if run as a script or by 'python -m pytest'
    # we trigger the below "else" condition by the following import
    import wooqi_pytest
    raise SystemExit(wooqi_pytest.main())
else:

    from wooqi.pytest._pytest.compat import _setup_collect_fakemodule
    _preloadplugins()  # to populate pytest.* namespace so help(pytest) works
    _setup_collect_fakemodule()
