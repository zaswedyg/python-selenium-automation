from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage(Page):
    NEW_ARRIVALS = (By.XPATH,'//*[@id="nav-subnav"]/a[7]')
    NEW_ARRIVALS_ITEMS = (By.CSS_SELECTOR, "div[id*='nav-flyout-aj:https://softlines-trova.s3-us-west-2.amazonaws.com/prod/US/mediaservice/megamenucreator_basic_en_US.json:subnav-sl-megamenu-8:0'] .mm-column")

    def open_product_page(self, product_id):
        self.open_url('https://www.amazon.com/gp/product/'+ product_id)

    def hover_over_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_user_can_see_new_arrivals_deals(self):
        assert self.find_elements(*self.NEW_ARRIVALS_ITEMS), f'Deals are not found'