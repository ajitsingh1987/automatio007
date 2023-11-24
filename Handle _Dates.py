from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options=Options()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,"hasDatepicker").click()
#driver.find_element(By.XPATH,"//a[text()='25']").click()
all_dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//a")
for date_element in all_dates:
    date=date_element.text
    print(date_element.text)
    if date=='25':
       date_element.click()
       break


