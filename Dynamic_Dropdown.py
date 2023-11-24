import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.ui import EC
from Browser_Opening import driver

# Locate the input field and send keys
input_field = driver.find_element(By.XPATH, "//input[@placeholder='Type to Select Countries']")
input_field.send_keys("ind")

# Wait for the autocomplete options to appear
wait = WebDriverWait(driver, 5)
autocomplete_options = wait.until(EC.visibility_of_all_elements_located((By.ID, "ui-id-39")))
# Adjust the CSS selector based on the structure of your autocomplete options

# Click on the desired option (in this case, the second option, index 1)
if len(autocomplete_options) > 1:
    autocomplete_options[0].click()



