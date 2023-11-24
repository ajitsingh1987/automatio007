from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Static_DropDown=driver.find_element(By.ID,"dropdown-class-example")
select = Select(Static_DropDown)
select.select_by_visible_text("Option3")
print(select.first_selected_option.text)
for i in select.options:
    print(i.text)
