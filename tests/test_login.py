import time

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.login_utils import login_error_messages
from utils.login_utils.log_utils import perform_login

@pytest.mark.parametrize("json_data",["login_user.json"],indirect=True)
def test_valid_login_credentials(browser,base_url,json_data):
    user = next(u for u in json_data if u["valid"])
    home_page = HomePage(browser)

    login_page = perform_login(
        browser,
        base_url,
        username=user["username"],
        password=user["password"]
    )

    login_page.submit_login()
    display_username = home_page.get_logged_in_username()

    assert user["username"] in display_username, (
        f"Expected username: '{user["username"]}' ,actual: '{display_username}'"
    )

@pytest.mark.parametrize("json_data",["login_user.json"],indirect=True)
def test_empty_username(browser,base_url,json_data):
    user = next(u for u in json_data if not u["valid"] and u["scenario"] == "empty username")

    login_page = perform_login(
        browser,
        base_url,
        username=user["username"],
        password=user["password"]
    )
    login_page.submit_login()

    assert login_page.get_field_error_text("username") == login_error_messages.USERNAME_ERROR_MESSAGE

@pytest.mark.parametrize("json_data",["login_user.json"],indirect=True)
def test_empty_password(browser,base_url,json_data):
    user = next(u for u in json_data if not u["valid"] and u["scenario"] == "empty password")

    login_page = perform_login(
        browser,
        base_url,
        username=user["username"],
        password=user["password"]
    )
    login_page.submit_login()

    assert login_page.get_field_error_text("password") == login_error_messages.PASSWORD_ERROR_MESSAGE

@pytest.mark.parametrize("json_data",["login_user.json"],indirect=True)
def test_invalid_login_credentials(browser,base_url,json_data):
    user = next(u for u in json_data if not u["valid"] and u["scenario"] == "invalid login credentials")

    login_page = perform_login(
        browser,
        base_url,
        username=user["username"],
        password=user["password"]
    )

    login_page.submit_login()
    time.sleep(3)
    assert login_page.get_field_error_text("invalid_login") == login_error_messages.WRONG_CREDENTIALS_ERROR_MESSAGE
