from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    SHIPPING_ADDRESS_FIELD = (By.ID, "shipping-address")
    PAYMENT_METHOD_FIELD = (By.ID, "payment-method")
    PLACE_ORDER_BUTTON = (By.ID, "place-order-button")

    def enter_shipping_address(self, address):
        self.enter_text(self.SHIPPING_ADDRESS_FIELD, address)

    def select_payment_method(self, method):
        self.enter_text(self.PAYMENT_METHOD_FIELD, method)

    def place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)
