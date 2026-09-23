"""Pytest plugin for build metadata validation."""
from .checker import check_metadata


def pytest_configure(config):
    issues = check_metadata("docs")
    markers = getattr(config, "addinivalue_line", lambda *a: None)
    markers("markers", "buildmeta: build metadata consistency marker")
    return issues
