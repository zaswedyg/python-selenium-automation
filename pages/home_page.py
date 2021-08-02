from pages.base_page import Page


class Home(Page):

    def open_home_page(self):
        self.open_url(url = 'https://www.amazon.com/')