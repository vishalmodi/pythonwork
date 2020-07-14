
from lib.cities.cities_page import CitiesPage
from tests.base_selenium_test import BaseSeleniumTest


class MyTestCase(BaseSeleniumTest):
    product_url = "https://www.lyft.com/rider/cities"

    @classmethod
    def setUpClass(cls) -> None:
        BaseSeleniumTest.setUpClass()

    def setUp(self) -> None:
        self.driver.get(self.product_url)
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        self.driver.close()

    def test_something(self):
        cities_page = CitiesPage(self.driver)
        search = cities_page.search_control()
        self.assertEqual(search.search_input_elem.is_displayed(), True)
        self.assertEqual(search.search_button_elem.is_displayed(), True)

        # enter search key
        city = "Seattle"
        search.search_for(city)
        self.driver.implicitly_wait(5)
        self.assertEqual(search.get_search_value(), city)

        #clicke on search icon
        search.search_button_elem.click()








