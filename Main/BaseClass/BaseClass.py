import pytest

from Main.DataProvider.ReadConfiguration import ReadConfiguration

pytest.mark.usefixtures("baseDriver")
class BaseClass():
    # A virtual driver has been created here
    def open_application(self):

        """Before Configuration file."""
        # self.driver.maximize_window()
        # self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        # self.driver.implicitly_wait(5)

        '''After creating configuration file, reading above values from configuration.ini file
         via ReadConfiguration '''
        # Values are coming from configuration.ini file via ReadConfiguration
        objReadConfiguration = ReadConfiguration()
        if objReadConfiguration.getMaximizeBrowser() == "True":
            self.driver.maximize_window()
        self.driver.get(objReadConfiguration.getApplicationUrl())
        self.driver.implicitly_wait(objReadConfiguration.getImplicitWait())
