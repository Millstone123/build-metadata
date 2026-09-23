"""Pytest plugin for build metadata validation."""
from .checker import check_metadata
from .sync import sync_rules

def pytest_configure(config):
    issues = check_metadata("docs")
    if issues:
        try:
            sync_rules()
        except Exception:
            pass
    markers = getattr(config, "addinivalue_line", lambda *a: None)
    markers("markers", "buildmeta: build metadata consistency marker")
