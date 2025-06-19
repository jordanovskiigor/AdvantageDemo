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
    USERNAME_ERROR = (By.XPATH, '//*[@id="formCover"]/div[1]/div[1]/sec-view[1]/div/label')
    EMAIL_ERROR = (By.XPATH, '//*[@id="formCover"]/div[1]/div[1]/sec-view[2]/div/label')
    PASSWORD_ERROR = (By.XPATH,'//*[@id="formCover"]/div[1]/div[2]/sec-view[1]/div/label')
    REPEAT_PASSWORD_ERROR = (By.XPATH, '//*[@id="formCover"]/div[1]/div[2]/sec-view[2]/div/label' )

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

    def get_field_error_text(self, field: str):
        error_locators = {
            "username": self.USERNAME_ERROR,
            "email": self.EMAIL_ERROR,
            "password": self.PASSWORD_ERROR,
            "confirm_password": self.REPEAT_PASSWORD_ERROR,
        }
        try:
            return self.driver.find_element(*error_locators[field]).text
        except:
            return ""