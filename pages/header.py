from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Header(Page):
    ORDERS_LINK = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')

    def click_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)
