from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product")  # Or whatever identifies the product block
    ADD_TO_CART_BTN = (By.NAME, "save_to_cart")
    CART_ICON = (By.ID, "menuCart")  # Optional: verify cart updated

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_first_product(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT)).click()

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN)).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()
