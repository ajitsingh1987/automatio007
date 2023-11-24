import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://www.yatra.com/")
driver.find_element(By.XPATH,"//*[@id='BE_flight_origin_date']").click()
time.sleep(3)
#driver.find_element(By.XPATH,"//*[@id='25/11/2023']").click()

all_dates=driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
for date in all_dates:
    if date.get_attribute("data-date") == "25/11/2023":
        date.click()
        time.sleep(3)
        break




