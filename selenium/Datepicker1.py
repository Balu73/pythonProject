
# in this we are going to learn Datepicker(if it have drop down formate)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.support.select import Select
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

srv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")
driver = webdriver.Chrome(service=srv_obj, options=options)
driver.get("https://dummyflights.com/?gclid=Cj0KCQiAorKfBhC0ARIsAHDzslup3qn2rxSeuSl8I4ffGHFyI1ye87P9NQ6riGfn0-S5eclGBHetYI8aAgLzEALw_wcB#one_way")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "One-way")
driver.find_element(By.XPATH, "//input[@id='flight-departure-date']").click()
month = driver.find_element(By.XPATH, '//select[@class = "monthselect" and  @xpath ="1"]')
year = driver.find_element(By.XPATH,'//select[@class = "yearselect" and  @xpath ="1"]')
datepicker_month = Select(month)
datepicker_month.select_by_index(3)
datepicker_month = Select(year)
datepicker_month.select_by_value("2024")
all_dates = driver.find_elements()