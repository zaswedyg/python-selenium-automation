from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Cart(Page):
    CART_IS_EMPTY_TEXT = (By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty' )]")

    def verify_cart_is_empty_text(self):
        self.verify_text('Your Amazon Cart is empty', *self.CART_IS_EMPTY_TEXT)
