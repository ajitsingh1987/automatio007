from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
CB=driver.find_elements(By.XPATH,"//input[starts-with(@name,'checkBoxOption')]")
print(CB)
print(len(CB))
for Check_Box in CB:
    Check_Box.click()

