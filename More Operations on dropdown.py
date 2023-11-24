from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Static_DropDown=driver.find_element(By.ID,"dropdown-class-example")
select=Select(Static_DropDown)
select.select_by_visible_text("Option1")
# Print First selected Option from Dropdown :
print(select.first_selected_option.text)
# Print all option from dropdown:
for i in select.options:
    print(i.text)

