from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

@given('Open page')
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Search for Cancel Order')
def search_keyword(context):
    context.driver.find_element(By.ID,"helpsearch").send_keys("Cancel Order", Keys.ENTER)

@then('Verify Cancel Order is displayed')
def verify_cancel_order(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR,"h1").text
    expected_text = "Cancel Items or Orders"
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

