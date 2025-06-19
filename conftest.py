import json
import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="session")
def config():
    with open("config/config.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]

@pytest.fixture(scope="function")
def browser(config):
    browser_type = config.get("browser","chrome")

    if browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser type: ${browser_type}")

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def json_data(request):
    filename = request.param
    file_path = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(file_path) as f:
        return json.load(f)