from Main.PageObjects.HomePage import HomePage


class HomeMethods:

    def __init__(self, driver):
        self.driver = driver
        self.objHomePage = HomePage(self.driver)

    def ClickAddToCartBrocolli(self):
        self.objHomePage.getAddToCart().click()

    def ClickToProceedToCheckoutBtn(self):
        self.objHomePage.getProceedToCheckoutBtn().click()

    def ClickToCart(self):
        self.objHomePage.getCartIcon().click()