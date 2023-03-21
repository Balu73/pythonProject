from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

ser_obj = Service(r"F:\python new version\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(3)

f = driver.find_element(By.XPATH, '//div[text() = "Fashion"]')
mtw = driver.find_element(By.XPATH,"//a[contains(text(),'Login')]")


action = ActionChains(driver)

time.sleep(3)