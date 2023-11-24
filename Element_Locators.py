from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Locate element By ID:
#driver.find_element(By.ID,"checkBoxOption1").click()
# Locate element By NAME:
#driver.find_element(By.NAME,"checkBoxOption2").click()
# Locate element By CLASS NAME:
#driver.find_element(By.CLASS_NAME,"radioButton").click()
# Locate element By LINK TEXT:
#driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
# Locate element By PARTIAL LINK TEXT:
#driver.find_element(By.PARTIAL_LINK_TEXT,"InterviewQues/ResumeAssistance/").click()

