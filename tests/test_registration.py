import os
import json
import random
from audioop import error
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.register_utils import perform_registration
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils import error_messages

@pytest.mark.parametrize("json_data", ["registration_user.json"], indirect=True)
def test_valid_registration(browser, base_url,json_data):
    user = next(u for u in json_data if u["valid"])

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

@pytest.mark.parametrize("json_data", ["registration_user.json"], indirect=True)
def test_registration_with_empty_required_field(browser, base_url, json_data):
    user = next(u for u in json_data if not u["valid"] and u["scenario"] == "empty username")

    reg_page = perform_registration(
        browser,
        base_url,
        username=user["username"],
        email="email@test.com",
        password=user["password"],
        confirm_password=user["confirm_password"],
    )

    assert reg_page.get_field_error_text("username") == error_messages.USERNAME_ERROR_MESSAGE

@pytest.mark.parametrize("json_data",["registration_user.json"],indirect=True)
def test_registration_invalid_email(browser,base_url,json_data):
    user = next(u for u in json_data if not u["valid"] and u["scenario"] == "invalid email format")

    reg_page = perform_registration(
        browser,
        base_url,
        username=user["username"],
        email=user["username"],
        password=user["password"],
        confirm_password=user["confirm_password"],
    )

    assert reg_page.get_field_error_text("email") == error_messages.EMAIL_ERROR_FORMAT_MESSAGE

@pytest.mark.parametrize("json_data", ["registration_user.json"], indirect=True)
def test_registration_with_invalid_password_format(browser, base_url, json_data):
    user = next(u for u in json_data if not u["valid"] and u["scenario"] == "invalid password format")

    reg_page = perform_registration(
        browser,
        base_url,
        username=user["username"],
        email=f"{user["username"]}@test.com",
        password=user["password"],
        confirm_password=user["confirm_password"],
    )

    assert reg_page.get_field_error_text("password") == error_messages.PASSWORD_ERROR_FORMAT_MESSAGE


