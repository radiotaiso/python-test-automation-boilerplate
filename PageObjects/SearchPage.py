from Locators.SearchLocators import SearchLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class Search(BasePage):

    def set_query(self):
        element = self.driver.find_element(*SearchLocators.SEARCH_INPUT)
        element.send_keys("Selenium with Python")

    def click_search(self):
        element = self.driver.find_element(*SearchLocators.SEARCH_BUTTON)
        element.click()

    def results_visible(self):
        element = self.driver.find_element(*SearchLocators.SEARCH_RESULTS)
        if element:
            return True

