import json
import random

import playwright
import pytest

#Configure Environment
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Environment: qa/uat")

@pytest.fixture(scope="session")
def config(pytestconfig):
    env = pytestconfig.getoption("env")
    config_path = f"config/{env}.json"
    with open(config_path) as f:
        return json.load(f)

@pytest.fixture(scope="session")
def api_context(playwright, config):
    base_url = config["book_library_baseurl"]
    return playwright.request.new_context(base_url=base_url)

@pytest.fixture(scope="function")
def add_book():
    return {
        "endpoint": "/Library/Addbook.php",
        "payload": {
            "name": "Learn Appium Automation with Java",
            "isbn": "QE",
            "aisle": str(random.randint(100, 999)),
            "author": "John foe"
        }
    }


