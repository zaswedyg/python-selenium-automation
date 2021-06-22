from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/Users\yurka\Desktop\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# Open the url

driver.get("https://www.amazon.com/gp/help/customer/display.html ")


# Search for cancel order

driver.find_element(By.ID,"helpsearch").send_keys("Cancel Order", Keys.ENTER)

# Verify ‘Cancel Items or Orders’ text is present

actual_text = driver.find_element(By.XPATH,"//div[@class='help-content']/h1").text
expected_text = "Cancel Items or Orders"

assert expected_text == actual_text, f'The expected text is {expected_text}, but we got {actual_text}'


# quit browser

driver.quit()

