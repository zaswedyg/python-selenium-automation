from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on cart')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'#nav-cart').click()

@then('Verify cart is empty')
def check_empty_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"div[class*='empty'] h2")