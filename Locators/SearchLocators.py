from selenium.webdriver.common.by import By


class SearchLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_BUTTON = (By.NAME, 'btnK')
    SEARCH_RESULTS = (By.CLASS_NAME, 'med')

    EMAIL_BOX = (By.ID, "email")
    PASS_BOX = (By.ID, "pass")
    LOGIN_SUBMIT = (By.ID, "loginbutton")
    NEW_MSG_BUTTON = (By.XPATH, "//a[@title='New Message']")