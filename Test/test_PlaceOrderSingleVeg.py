import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Main.BaseClass.BaseClass import BaseClass
from Main.PageMethods.CartMethods import CartMethods
from Main.PageMethods.CountryMethods import CountryMethods
from Main.PageMethods.HomeMethods import HomeMethods


class Test_PlaceOrderSingleVeg(BaseClass):

    @pytest.mark.browserValue('chrome')
    def test_placeOrder(self):
        # cwd = os.getcwd()
        # driver_path = cwd+"/MainResource/BrowserDriver/chromedriver"
        # driver = webdriver.Chrome(executable_path=driver_path)
        #
        # self.driver.maximize_window()
        # self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        # self.driver.implicitly_wait(5)
        # self.open_application()
        # # Click on Add to cart button
        # self.driver.find_element_by_xpath("//button[text()='ADD TO CART'][1]").click()
        #
        # # Click on cart icon
        # self.driver.find_element_by_xpath("//a[@class='cart-icon']/img").click()
        #
        # # Click on popup PROCEED TO CHECKOUT
        # self.driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
        #
        # # Click on place order
        # self.driver.find_element_by_xpath("//button[text()='Place Order']").click()
        #
        # # Selecting country from drop down
        # dropDown = self.driver.find_element_by_xpath("//select[@style='width: 200px;']")
        # select = Select(dropDown)
        # select.select_by_value("India")
        #
        # # Click on Agree checkbox
        # self.driver.find_element_by_xpath("//input[@type = 'checkbox']").click()
        #
        # # Click on Proceed button
        # self.driver.find_element_by_xpath("//button[text()= 'Proceed']").click()

        objHomeMethods = HomeMethods(self.driver)
        objCartMethods = CartMethods(self.driver)
        objCountryMethods = CountryMethods(self.driver)

        self.open_application()
        objHomeMethods.ClickAddToCartBrocolli()
        objHomeMethods.ClickToCart()
        objHomeMethods.ClickToProceedToCheckoutBtn()

        objCartMethods.ClickOnPlaceOrderBtn()

        time.sleep(3)
        dropDown = objCountryMethods.selectCountry()
        select = Select(dropDown)
        select.select_by_value("India")

        time.sleep(3)
        objCountryMethods.ClickAgreeCheckbox()

        time.sleep(3)
        objCountryMethods.ClickOnProceedBtn()




