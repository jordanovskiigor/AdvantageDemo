from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    ACCOUNT_ICON = (By.ID, "menuUserLink")
    CREATE_ACCOUNT_BTN = (By.LINK_TEXT, "CREATE NEW ACCOUNT")
    USERNAME_INPUT = (By.NAME, "usernameRegisterPage")
    LOGGED_IN_USERNAME = (By.XPATH, '//*[@id="menuUserLink"]/span')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_registration_form(self):
        self.driver.find_element(*self.ACCOUNT_ICON).click()
        self.wait.until(EC.visibility_of_element_located(self.CREATE_ACCOUNT_BTN)).click()
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        return self

    def get_logged_in_username(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGGED_IN_USERNAME))
        return self.driver.find_element(*self.LOGGED_IN_USERNAME).text