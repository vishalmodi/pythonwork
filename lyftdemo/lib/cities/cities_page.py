from lib.base_page import BasePage
from lib.controls.search import SearchControl


class CitiesPage(BasePage):
    def __init__(self, driver):
        super(CitiesPage, self).__init__(driver)

    def search_control(self):
        search = SearchControl(self.driver)
        return search

