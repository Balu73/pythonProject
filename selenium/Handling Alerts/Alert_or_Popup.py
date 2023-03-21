import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

serv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")
driver = webdriver.Chrome(options=options, service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]').click()
# By using following code we can switch to alert window
Alert_window = driver.switch_to.alert
Alert_window.send_keys("Hi, Balakrishna Bandari")
print(Alert_window.text)
Alert_window.accept()  # here accept() = Ok or confirm, dismiss() = Cancel
time.sleep(5)
driver.quit()