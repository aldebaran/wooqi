# -*- coding: utf-8 -*-
"""
General plugin file
"""
import pytest


def pytest_addoption(parser):
    """
    Configuration of pytest parsing
    """
    group = parser.getgroup('general')
    group.addoption(
        "--seq_config",
        default=None,
        action="store",
        help="Test file config"
    )


@pytest.fixture(scope="session")
def test_config(request):
    """
    Test config
    """
    return request.config.getoption("--seq_config")
