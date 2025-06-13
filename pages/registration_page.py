from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class RegistrationPage:
    USERNAME_INPUT = (By.NAME, "usernameRegisterPage")
    EMAIL_INPUT = (By.NAME, "emailRegisterPage")
    PASSWORD_INPUT = (By.NAME, "passwordRegisterPage")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "confirm_passwordRegisterPage")
    TERMS_CHECKBOX = (By.NAME, "i_agree")
    REGISTER_BUTTON = (By.ID, "register_btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))

    def fill_registration_form(self, username, email, password, confirm_password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        time.sleep(1)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        time.sleep(1)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(confirm_password)
        time.sleep(1)

    def accept_terms(self):
        checkbox = self.driver.find_element(*self.TERMS_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()
            time.sleep(1)

    def submit_registration(self):
        self.accept_terms()
        self.driver.find_element(*self.REGISTER_BUTTON).click()