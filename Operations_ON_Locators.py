from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Input_field=driver.find_element(By.XPATH,"//input[@id='name']")
Input_field.send_keys("Ajeet")
Input_field.clear()
Input_field.send_keys("Rahul")
# For retriving Text
Alert_example = driver.find_element(By.XPATH, "//legend[text()='Switch To Alert Example']")
Alert_example_text = Alert_example.text
print(Alert_example_text)

Suggetion_Class_Example = driver.find_element(By.XPATH, "//legend[text()='Suggession Class Example']")
S = Suggetion_Class_Example.text
print(S)
