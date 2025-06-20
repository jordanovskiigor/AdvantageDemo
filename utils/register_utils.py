from pages.registration_page import RegistrationPage
from pages.home_page import HomePage
from selenium import webdriver
from selenium.webdriver.common.by import By

def perform_registration(browser,base_url,username,email,password,confirm_password):
    browser.get(base_url)

    home_page = HomePage(browser)
    home_page.go_to_registration_form()

    reg_page = RegistrationPage(browser)
    reg_page.fill_registration_form(
        username=username,
        email=email,
        password=password,
        confirm_password=confirm_password,
    )
    browser.find_element(By.TAG_NAME, "body").click()
    return reg_page
