from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
import time

serv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")
driver = webdriver.Chrome(options=options, service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#To click link

#Approch 1

#driver.find_element(By.LINK_TEXT, "Digital downloads").click()

#Approch 2

#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital ").click()

#To Get all the links on web page using following steps

Links = driver.find_elements(By.TAG_NAME, "a")
print(len(Links))
for Link in Links:
    print(Link.text)
