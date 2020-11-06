from selenium.webdriver.common.by import By


class CountryPage():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    selectDropdown = (By.XPATH, "//select[@style='width: 200px;']")
    agreeCheckbox = (By.XPATH, "//input[@type = 'checkbox']")
    proceedBtn = (By.XPATH, "//button[text()= 'Proceed']")

    def getSelectDropdown(self):
        return self.driver.find_element(*self.selectDropdown)

    def getAgreeCheckbox(self):
        return self.driver.find_element(*self.agreeCheckbox)

    def getProceedBtn(self):
        return self.driver.find_element(*self.proceedBtn)
