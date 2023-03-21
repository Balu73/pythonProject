from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
serv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@name="username"]').send_keys("Admin")
driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys("admin123")
driver.find_element(By.XPATH, '//button[@type="submit"]')