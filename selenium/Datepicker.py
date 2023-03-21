from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions, Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

srv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")
driver = webdriver.Chrome(service=srv_obj, options=options)
driver.get("https://www.globalsqa.com/demo-site/datepicker/")
driver.maximize_window()
driver.switch_to.frame(3) # here arugument passed "3" becauese it the frame in website it's 4th frame(starting position is 0) that's why
year = "2022"
month = "March"
date = "21"
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
# The following script is for select the month and year in calender
while True:
    MM= driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    yyyy =driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
    if MM == month and yyyy == year:
        break;
    else:
        driver.find_element(By.XPATH, "//span[contains(text(),'Prev')]").click() # previous button
# The following script is for select the date in calender

All_dates = driver.find_elements(By.XPATH, "//body/div[@id='ui-datepicker-div']/table[1]/tbody/tr/td/a")
for ele in All_dates:
    if ele.text == date:
        ele.click()
        break

