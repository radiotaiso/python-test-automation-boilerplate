from Elements.Element import BasePageElement
from Locators.LoginLocators import LoginLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def click_login(self):
        element = self.driver.find_element(*LoginLocators.LOGIN_BUTTON)
        element.click()


class Login(BasePage):

    def set_username(self):
        element = self.driver.find_element(*LoginLocators.USERNAME)
        element.send_keys("USERNAME")

    def set_password(self):
        element = self.driver.find_element(*LoginLocators.PASSWORD)
        element.send_keys("PASSWORD")


