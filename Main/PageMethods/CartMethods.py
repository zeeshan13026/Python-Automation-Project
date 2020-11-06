from Main.PageObjects.CartPage import CartPage


class CartMethods:
    def __init__(self, driver):
        self.driver = driver
        self.objCartPage = CartPage(self.driver)

    def ClickOnPlaceOrderBtn(self):
        self.objCartPage.getPlaceOrderBtn().click()

    def ApplyCoupon(self, coupon):
        self.objCartPage.getPromoCodeTextField().send_keys(coupon)
        self.objCartPage.getApplyCouponBtn().click()
