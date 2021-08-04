from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify user can click through colors')
def click_through_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage', 'Light Wash', 'Medium Vintage', 'Medium Wash',
                       'Rinse', 'Rinsed Vintage', 'Vintage Light Wash', 'Washed Black', 'Bright White', 'Dark Khaki', 'Light Khaki', 'Olive', 'Sage Green']
    actual_colors = context.driver.find_elements(By.CSS_SELECTOR,"#variation_color_name li")

    for i in range(len(actual_colors)):
        actual_colors[i].click()
        actual_text = context.driver.find_element(By.CSS_SELECTOR, "span.selection").text
        assert expected_colors[i] == actual_text, f'Actual text is {actual_text}, but expected {expected_colors[i]}'