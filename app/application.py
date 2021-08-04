from pages.header import Header
from pages.home_page import Home
from pages.sign_in import SignIn
from pages.cart import Cart
from pages.product_page import ProductPage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.home_page = Home(self.driver)
        self.header = Header(self.driver)
        self.sign_in = SignIn(self.driver)
        self.cart = Cart(self.driver)
        self.product_page = ProductPage(self.driver)