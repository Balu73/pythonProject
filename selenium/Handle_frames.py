import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

serv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")
driver = webdriver.Chrome(options=options, service=serv_obj)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

# switch_to.frame("name of the frame")
# switch_to.frame("id of the frame")
# switch_to.frame(webelement)
# switch_to.frame(index)


driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(3)
# Here if want to switch another frame we need to go first to the main page for that we need to use the following code
driver.switch_to.default_content()
print(" ok ")

time.sleep(5)

driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH,"//body[1]/main[1]/div[1]/section[1]/ul[1]/li[14]/a[1]/span[1]").click()
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, '//li/a[text() = "Index"]').click()
driver.quit()
