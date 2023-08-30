from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "search-box")
    LOGIN_BUTTON = (By.ID, "login-button")

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_BOX, product_name)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
