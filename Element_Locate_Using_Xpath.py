from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Locate element By Xpath using normal Xpath Syntax : //tagname[@attribute='value']
#driver.find_element(By.XPATH,"//input[@value='radio2']").click()
# Locate element By Xpath using 2 attributes and value Syntax : //tagname[@attribute1='value' AND/OR @attribute2='value']
#driver.find_element(By.XPATH, "//input[@value='radio2' and @name='radioButton']").click()
# Locate element By Xpath using TEXT : //tagname[text()='type text here']
#driver.find_element(By.XPATH,"//a[text()='Free Access to InterviewQues/ResumeAssistance/Material']").click()
# Locate element By Xpath using STARTS-WITH : //tagname[starts-with(@attribute,'starting values')]
#driver.find_element(By.XPATH,"//a[starts-with(@class,'btn-style')]").click()
# Locate element By Xpath using Contains : //tagname[contains(@attribute,'starting values')]
#driver.find_element(By.XPATH,"//a[contains(text(),' InterviewQues/ResumeAssistance/Material')]").click()
# Locate element By Xpath using Partial Text : //tagname[contains/starts-with(@text(),'partial text here')]
driver.find_element(By.XPATH,"//legend[contains(text(),'Class Example')]")
