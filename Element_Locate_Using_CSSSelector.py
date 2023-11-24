from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Locate element By CSS SELECTOR Using ID:Syntax: tagname#IDValue
#driver.find_element(By.CSS_SELECTOR,"input#name").send_keys("Ajeet Yadav")
# Locate element By CSS SELECTOR Using Attribute & Value Syntax : tagname[attribute='value']
#driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Your Name']").send_keys("Appu")
# Locate element By CSS SELECTOR Using Class , Attribute & Value Syntax : tagname.class_value[attribute='value']
#driver.find_element(By.CSS_SELECTOR,"input.inputs[name='enter-name']").send_keys("JAVA")
# Locate element By CSS SELECTOR Using Class Syntax: tagname.classvalue
driver.find_element(By.CSS_SELECTOR,"button#openwindow").click()
