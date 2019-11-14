from Locators.SearchLocators import SearchLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class Search(BasePage):

    def set_query(self):
        element = self.driver.find_element(*SearchLocators.SEARCH_INPUT)
        element.send_keys("Selenium with Python")

    def click_login(self):
        element = self.driver.find_element(*SearchLocators.LOGIN_SUBMIT)
        element.click()

    def results_visible(self):
        element = self.driver.find_element(*SearchLocators.NEW_MSG_BUTTON)
        if element:
            return True

    def set_user(self):
        element = self.driver.find_element(*SearchLocators.EMAIL_BOX)
        element.send_keys("uriel@yalochat.com")

    def set_pass(self):
        element = self.driver.find_element(*SearchLocators.PASS_BOX)
        element.send_keys("")