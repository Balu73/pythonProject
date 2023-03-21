from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service_obj = Service(r"F:\python new version\Scripts\chromedriver.exe")
driver=webdriver.Chrome()
driver.implicitly_wait(7)
driver.get("https://demo.automationtesting.in/Index.html")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Sign In").click()
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/input").send_keys("Admin")
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/input").send_keys("admini123")
driver.find_element(By.ID, "enterbtn").click()

driver.close()


print("Login Test Passed")

