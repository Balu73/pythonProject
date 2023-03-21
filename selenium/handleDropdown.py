import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ChromeOptions, Chrome

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

serv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=serv_obj)
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")

drp_country_ele = driver.find_element(By.TAG_NAME, 'select')
drp_country = Select(drp_country_ele)

# select item from the drop_drown list by using value
# drp_country.select_by_value("4") # American Samoa

# select item from the drop_down list by using index
# drp_country.select_by_index(14) #Astria

# select item from the drop_down list by using Text
# drp_country.select_by_visible_text("India")

# To select all item inn drop down list
all_option = drp_country.options
print("Total number of options available is: ", len(all_option))
# To select the option from drop down list without using builtin function
for opt in all_option:
    if opt.text == "India":
        opt.click()
        break


time.sleep(5)
print("successfully finished")