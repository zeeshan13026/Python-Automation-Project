import os

from selenium import webdriver
from selenium.webdriver.support.select import Select

class Test_PlaceOrderSingleVeg:
    def test_placeOrder(self):
        cwd = os.getcwd()
        driver_path = cwd+"/MainResource/BrowserDriver/chromedriver"
        driver = webdriver.Chrome(executable_path=driver_path)

        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.implicitly_wait(5)

        # Click on Add to cart button
        driver.find_element_by_xpath("//button[text()='ADD TO CART'][1]").click()

        # Click on cart icon
        driver.find_element_by_xpath("//a[@class='cart-icon']/img").click()

        # Click on popup PROCEED TO CHECKOUT
        driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

        # Click on place order
        driver.find_element_by_xpath("//button[text()='Place Order']").click()

        # Selecting country from drop down
        dropDown = driver.find_element_by_xpath("//select[@style='width: 200px;']")
        select = Select(dropDown)
        select.select_by_value("India")

        # Click on Agree checkbox
        driver.find_element_by_xpath("//input[@type = 'checkbox']").click()

        # Click on Proceed button
        driver.find_element_by_xpath("//button[text()= 'Proceed']").click()



