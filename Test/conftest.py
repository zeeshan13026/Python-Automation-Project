import os

import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def baseDriver(request):
    marker = request.node.get_closest_marker('browserValue')
    print("Marker : ", marker)
    cwd = os.getcwd()
    driver_path = cwd + "/MainResource/BrowserDriver/"

    if marker:
        if marker.args[0] == 'chrome':
            driver = webdriver.Chrome(executable_path=driver_path + 'chromedriver')
        elif marker.args[0] == 'firefox':
            driver = webdriver.Firefox(executable_path=driver_path + 'geckodriver')
        else:
            pytest.skip('Browser not implemented')

    else:
        pytest.skip('Browser not passed')

    request.cls.driver = driver
    yield
    driver.quit()
