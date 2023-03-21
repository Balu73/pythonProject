from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ops = webdriver.ChromeOptions()  # This is we can use some advanced settings on browser
ops.add_argument("--disable-notifications")  # By using this we can ignore browser notification popUps
ops.add_experimental_option("detach", True)

serv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")

driver = webdriver.Chrome(service=serv_obj, options=ops)

driver.get('https://www.gps-coordinates.net/my-location')
driver.maximize_window()
