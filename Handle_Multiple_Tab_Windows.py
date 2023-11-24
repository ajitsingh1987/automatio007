import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.window_handles)
print("*******************")
driver.find_element(By.ID,"openwindow").click()
time.sleep(2)
print(driver.window_handles)
print("*******************")
driver.find_element(By.ID,"opentab").click()
time.sleep(2)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[2])
driver.find_element(By.XPATH,"").click

