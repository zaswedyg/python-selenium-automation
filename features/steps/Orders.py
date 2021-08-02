from behave import given, when, then

@given('Open Amazon Page')
def open_amazon_page(context):
    context.app.home_page.open_home_page()

@when('Click Amazon Orders link')
def click_orders_link(context):
    context.app.header.click_orders_link()

@then('Verify Sign In page is opened')
def verify_signin_page_is_opened(context):
    context.app.sign_in.verify_signin_is_open()

