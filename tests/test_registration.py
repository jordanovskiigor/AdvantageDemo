import os
import json
import random
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "registration_user.json")
with open(file_path) as f:
    users = json.load(f)

def test_valid_registration(browser, base_url):
    user = next(u for u in users if u["valid"])

    browser.get(base_url)

    home_page = HomePage(browser)
    home_page.go_to_registration_form()

    # unique username creation
    final_username = f"{user['username']}_{random.randint(1000, 9999)}"

    reg_page = RegistrationPage(browser)
    reg_page.fill_registration_form(
        username=final_username,
        email=f"{final_username}@test.com",
        password=user["password"],
        confirm_password=user["confirm_password"],
    )
    reg_page.submit_registration()

    displayed_username = home_page.get_logged_in_username()
    print(f"Logged in username displayed: '{displayed_username}'")
    assert final_username in displayed_username, (
        f"Expected username: '{final_username}' ,actual: '{displayed_username}'"
    )

