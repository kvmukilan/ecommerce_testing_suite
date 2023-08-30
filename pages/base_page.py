from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
