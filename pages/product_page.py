from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    VIEW_CART_BUTTON = (By.ID, "view-cart-button")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def view_cart(self):
        self.click(self.VIEW_CART_BUTTON)
