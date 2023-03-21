from selenium import webdriver
from selenium.webdriver import ChromeOptions,Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
import time

serv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")
driver = webdriver.Chrome(options=options, service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

time.sleep(3)
#checkboxs = driver.find_element(By.CSS_SELECTOR, "#monday")
checkboxs = driver.find_elements(By.XPATH, '//input[@type="checkbox" and contains(@id, "day")]')
# above code line give list so we cann't click all webelements so we have to use the below following 3 codelines
print(len(checkboxs))

#To all the checkboxes
for i in range(len(checkboxs)):
    checkboxs[i].click()


# OR


#for checkbox in checkboxs:
#   checkbox.click()

# Select the multiple checkboxes by choice

#for checkbox in checkboxs:
#    week_name = checkbox.get_attribute("id")
#    print(week_name)
#    if week_name == "tuesday"  or week_name == "wednesday" or week_name == "saturday" or week_name == "sunday":
#       checkbox.click()


# To select last two checkboxes follow this method
#for i in range(len(checkboxs)-2, len(checkboxs)):
#    checkboxs[i].click()

#To un select the selected check boxes we need to follow the  below steps
for checkbox in checkboxs:
    if checkbox.is_selected():
        checkbox.click()