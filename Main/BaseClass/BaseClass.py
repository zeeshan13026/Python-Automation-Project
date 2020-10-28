import pytest

pytest.mark.usefixtures("baseDriver")
class BaseClass():

    def open_application(self):
        self.driver.maximize_window()
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.implicitly_wait(5)