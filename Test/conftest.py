import os
import datetime

import pytest
from selenium import webdriver


def pytest_cmdline_preparse(config, args):
    curr_time = datetime.datetime.now()
    # 2020_10_09_23_48_57.3294873849
    curr = str(curr_time).replace("-", "_").replace(" ", "_").replace(":", "_")
    #html_file = os.getcwd() + "/../Reports/" +get_current_date_time()  + "ReportFile.html"
    html_file = os.getcwd() + "/../Main/Reports/" + curr.split(".")[0] + "ReportFile.html"
    print(html_file)
    args.extend(['--html', html_file, '--self-contained-html'])
    #py.test --html:html_file


@pytest.fixture(autouse=True)
def baseDriver(request):
    marker = request.node.get_closest_marker('browserValue')
    print("Marker : ", marker)
    cwd = os.getcwd()
    driver_path = cwd + "/../MainResource/BrowserDriver/"

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
