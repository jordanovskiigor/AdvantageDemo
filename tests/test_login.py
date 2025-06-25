import time

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils import login_error_messages

@pytest.mark.parametrize("json_data",["login_user.json"],indirect=True)
def test_valid_login_credentials(browser,base_url,json_data):
    user = next(u for u in json_data if u["valid"])

    browser.get(base_url)
    home_page = HomePage(browser)
    home_page.go_to_login_form()

    login_page = LoginPage(browser)

    login_page.fill_login_form(
        username = user["username"],
        password= user["password"]
    )

    login_page.submit_login()
    display_username = home_page.get_logged_in_username()

    assert user["username"] in display_username, (
        f"Expected username: '{user["username"]}' ,actual: '{display_username}'"
    )

@pytest.mark.parametrize("json_data",["login_user.json"],indirect=True)
def test_empty_username(browser,base_url,json_data):
    user = next(u for u in json_data if not u["valid"] and u["scenario"] == "empty username")

    browser.get(base_url)
    home_page = HomePage(browser)
    home_page.go_to_login_form()

    login_page = LoginPage(browser)

    login_page.fill_login_form(
        username=user["username"],
        password=user["password"]
    )

    login_page.submit_login()

    assert login_page.get_field_error_text("username") == login_error_messages.USERNAME_ERROR_MESSAGE

@pytest.mark.parametrize("json_data",["login_user.json"],indirect=True)
def test_empty_password(browser,base_url,json_data):
    user = next(u for u in json_data if not u["valid"] and u["scenario"] == "empty password")

    browser.get(base_url)
    home_page = HomePage(browser)
    home_page.go_to_login_form()

    login_page = LoginPage(browser)

    login_page.fill_login_form(
        username=user["username"],
        password=user["password"]
    )

    login_page.submit_login()

    assert login_page.get_field_error_text("password") == login_error_messages.PASSWORD_ERROR_MESSAGE

@pytest.mark.parametrize("json_data",["login_user.json"],indirect=True)
def test_invalid_login_credentials(browser,base_url,json_data):
    user = next(u for u in json_data if not u["valid"] and u["scenario"] == "invalid login credentials")

    browser.get(base_url)
    home_page = HomePage(browser)
    home_page.go_to_login_form()

    login_page = LoginPage(browser)

    login_page.fill_login_form(
        username=user["username"],
        password=user["password"]
    )

    login_page.submit_login()
    time.sleep(3)
    assert login_page.get_field_error_text("invalid_login") == login_error_messages.WRONG_CREDENTIALS_ERROR_MESSAGE
