from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()

@then("Verify 'Your Amazon Cart is empty' text present")
def verify_cart_is_empty_text(context):
    context.app.cart.verify_cart_is_empty_text()
