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
driver.switch_to.frame('courses-iframe')
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[6]/a").click()
driver.switch_to.default_content()
driver.find_element(By.ID,"name").send_keys("Ajeet")
