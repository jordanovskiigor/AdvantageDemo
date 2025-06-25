from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID,"sign_in_btn")
    USERNAME_ERROR = (By.XPATH, '/html/body/login-modal/div/div/div[3]/sec-form/sec-view[1]/div/label')
    PASSWORD_ERROR = (By.XPATH, '/html/body/login-modal/div/div/div[3]/sec-form/sec-view[2]/div/label')
    INVALID_LOGIN_CREDENTIALS = (By.XPATH, '//*[@id="signInResultMessage"]')

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_login_form(self,username,password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        time.sleep(1)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        time.sleep(1)

    def submit_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_field_error_text(self,field:str):
        error_locators = {
            "username": self.USERNAME_ERROR,
            "password": self.PASSWORD_ERROR,
            "invalid_login": self.INVALID_LOGIN_CREDENTIALS
        }
        try:
            locator = error_locators[field]
            self.wait.until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator).text
        except:
            return ""