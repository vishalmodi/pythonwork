

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load(self):
        pass