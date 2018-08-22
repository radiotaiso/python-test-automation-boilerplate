from selenium.webdriver.common.by import By


class SearchLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_BUTTON = (By.CLASS_NAME, 'sbqs_c')
    SEARCH_RESULTS = (By.CLASS_NAME, 'med')
