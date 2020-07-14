import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseSeleniumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        selenium_grid_url = "http://0.0.0.0:4444/wd/hub"

        # Create a desired capabilities object as a starting point.
        capabilities = DesiredCapabilities.CHROME.copy()

        # Instantiate an instance of Remote WebDriver with the desired capabilities.
        cls.driver = webdriver.Remote(desired_capabilities=capabilities,
                                      command_executor=selenium_grid_url)


