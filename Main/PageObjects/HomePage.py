from selenium.webdriver.common.by import By


class HomePage():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    addToCart = (By.XPATH, "//button[text()='ADD TO CART'][1]")
    incrementQuantity = (By.XPATH, "//a[@class='increment'][1]")
    decrementQuantity = (By.XPATH, "//h4[text()='Brocolli - 1 Kg']/../div[2]/a[1]")
    cartIcon = (By.XPATH, "//a[@class='cart-icon']/img")
    proceedToCheckoutBtn = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def getAddToCart(self):
        return self.driver.find_element(*self.addToCart)

    def getIncrementQuantity(self):
        return self.driver.find_element(*self.incrementQuantity)

    def getDecrementQuantity(self):
        return self.driver.find_element(*self.decrementQuantity)

    def getCartIcon(self):
        return self.driver.find_element(*self.cartIcon)

    def getProceedToCheckoutBtn(self):
        return self.driver.find_element(*self.proceedToCheckoutBtn)
