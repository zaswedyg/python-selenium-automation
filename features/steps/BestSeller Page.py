from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

TOP_LINKS = (By.CSS_SELECTOR,'#zg_header li a')
HEADER = (By.ID, 'zg_banner_text')


@given('Open Best Sellers')
def best_sellers(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs')

@then('Verify {number} links are displayed')
def verify_links(context, number):
    actual_number = context.driver.find_elements(By.CSS_SELECTOR,'#zg_header li a')
    assert int(number) == len(actual_number), f'Expected {number}, but got {len(actual_number)}'

@then('Verify user can click through links')
def click_through_links(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for i in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[i]
        link_text = link.text
        link.click()
        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not in {header_text}'