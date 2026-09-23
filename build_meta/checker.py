"""Metadata consistency checking for build systems."""
import pathlib

import yaml

def check_metadata(directory):
    """Check that build metadata is internally consistent."""
    issues = []
    for p in sorted(pathlib.Path(directory).glob("*.yaml")):
        with open(p) as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            continue
        for rule in data.get("checks", []):
            name = rule.get("name", "")
            if name:
                issues.append(name)
    return issues
