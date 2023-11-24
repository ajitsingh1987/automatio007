from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Declare Explicit Wait
driver.exp
Static_DropDown=driver.find_element(By.ID,"dropdown-class-example")
select=Select(Static_DropDown)
# Select by Index
select.select_by_index(2)
# Select By Value
select.select_by_value('option1')
# Select By Visible Text
select.select_by_visible_text('Option3')
# How to select any value from dropdown while SELECT tag is no there
driver.find_element(By.XPATH,"//option[@value='option3']").click()

