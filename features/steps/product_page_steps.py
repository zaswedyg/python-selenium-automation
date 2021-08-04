from behave import given, when, then

@given('Open product {product_id} page')
def open_product_page(context, product_id):
    context.app.product_page.open_product_page(product_id)

@when('Hover over New Arrivals')
def hover_over_new_arrivals(context):
    context.app.product_page.hover_over_new_arrivals()

@then('Verify user can see New Arrivals Deals')
def user_can_see_new_arrivals_deals(context):
    context.app.product_page.verify_user_can_see_new_arrivals_deals()
