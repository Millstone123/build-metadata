import yaml

def test_checks_exist():
    data = yaml.safe_load(open("docs/checks.yaml"))
    assert len(data.get("checks", [])) > 0
    assert all("name" in c for c in data["checks"])
