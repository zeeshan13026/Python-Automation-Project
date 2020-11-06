from selenium.webdriver.common.by import By


class CartPage():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    applyCouponBtn = (By.XPATH, "//button[text()='Apply']")
    promoCodeTextField = (By.XPATH, "//input[@class='promoCode']")
    placeOrderBtn = (By.XPATH, "//button[text()='Place Order']")

    def getApplyCouponBtn(self):
        return self.driver.find_element(*self.applyCouponBtn)

    def getPromoCodeTextField(self):
        return self.driver.find_element(*self.promoCodeTextField)

    def getPlaceOrderBtn(self):
        return self.driver.find_element(*self.placeOrderBtn)
