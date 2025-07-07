from pages.home_page import HomePage
from pages.login_page import LoginPage


def perform_login(browser,base_url,username,password):
    browser.get(base_url)
    home_page = HomePage(browser)
    home_page.go_to_login_form()

    login_page = LoginPage(browser)
    login_page.fill_login_form(
        username=username,
        password=password
    )
    return login_page