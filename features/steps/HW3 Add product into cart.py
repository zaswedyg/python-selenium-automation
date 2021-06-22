from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open product page')
def product_page(context):
    context.driver.get('https://www.amazon.com/2021-Masters-Green-Caddy-Hat/dp/B092FRMXQL/ref=sr_1_1_sspa?dchild=1&keywords=hat&qid=1623896237&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVU5TOTZKQzhKTzFJJmVuY3J5cHRlZElkPUEwMjUwNjYyMVRQSEM5WjI4MEZVUiZlbmNyeXB0ZWRBZElkPUEwMzM0MzUwWUFCSVhCTDlRWE83JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==')

@when('Add product into cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'#add-to-cart-button').click()

@when('Open cart')
def open_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart').click()

@then('Verify product is added')
def added_product(context):
    context.driver.find_element(By.CSS_SELECTOR,"a#nav-cart[aria-label='1 item in cart']")