from pages.header import Header
from pages.home_page import Home
from pages.sign_in import SignIn
from pages.cart import Cart

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.home_page = Home(self.driver)
        self.header = Header(self.driver)
        self.sign_in = SignIn(self.driver)
        self.cart = Cart(self.driver)