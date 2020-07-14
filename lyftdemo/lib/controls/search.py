
from selenium import webdriver


class SearchControl:
    def __init__(self, driver):
        self.driver = driver
        self.input_loc = "//input[@name='search-cities']"
        self.parent_loc = "//input[@name='search-cities']/.."

    def get_parent_elem(self):
        return self.driver.find_element_by_xpath(self.parent_loc)

    # TODO - need to fix it.
    def search_button(self):
        return self.get_parent_elem().find_element_by_name("svg")

    def search_input_elem(self):
        return self.driver.find_element_by_xpath(self.input_loc)

    def search_for(self, value):
        self.search_input_elem().send_keys(value)

    def get_search_value(self):
        return self.search_input_elem().get_attribute('value')
