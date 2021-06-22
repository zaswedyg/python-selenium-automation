from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Best Sellers')
def best_sellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify {number} links are displayed')
def verify_links(context, number):
    actual_number = context.driver.find_elements(By.CSS_SELECTOR,'#zg_header li a')
    assert int(number) == len(actual_number), f'Expected {number}, but got {len(actual_number)}'