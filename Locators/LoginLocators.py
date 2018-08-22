from selenium.webdriver.common.by import By


class LoginLocators(object):
    """A class for main page locators. All main page locators should come here"""
    USERNAME = (By.NAME, 'USERNAME_LOCATOR')
    PASSWORD = (By.NAME, 'PASSWORD_LOCATOR')
    LOGIN_BUTTON = (By.CLASS_NAME, 'LOCATOR_LOGIN_BUTTON')