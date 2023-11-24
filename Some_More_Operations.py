from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Mouse Hover
action=ActionChains(driver, duration=2000)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.XPATH,"//a[contains(@href,'#top')]")).click().perform()
# Perform Double Click
action.move_to_element(driver.find_element(By.ID,"mousehover")).double_click().perform()
# Perform Right Click
action.move_to_element(driver.find_element(By.ID,"mousehover")).context_click().perform()
