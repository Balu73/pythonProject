from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
serv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=options)

driver.get("https://www.google.com/")
driver.maximize_window()
driver.f