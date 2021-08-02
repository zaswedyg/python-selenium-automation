from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SignIn(Page):

    def verify_signin_is_open(self):
        self.verify_url_contains_query(query = 'signin')