from Main.PageObjects.CountryPage import CountryPage


class CountryMethods:
    def __init__(self,driver):
        self.driver = driver
        self.objCountryPage = CountryPage(self.driver)


    def selectCountry(self):
        return self.objCountryPage.getSelectDropdown()

    def ClickAgreeCheckbox(self):
        self.objCountryPage.getAgreeCheckbox().click()

    def ClickOnProceedBtn(self):
        self.objCountryPage.getProceedBtn().click()


