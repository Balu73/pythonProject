from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
serv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
search_box=driver.find_element(By.NAME, "q")
driver.refresh()
radiobutton=driver.find_element(By.ID, "gender-male")
radiobutton.click()
# by using the is_displayed() method used to check any web element is visible or not
# by using the is_enabled() method used to check
print("Radiobutton is selected = ", radiobutton.is_selected())
print("Radiobutton is enable = ", radiobutton.is_enabled())
print("Radiobutton is displayed = ", radiobutton.is_displayed())

