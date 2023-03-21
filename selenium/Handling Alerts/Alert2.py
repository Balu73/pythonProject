import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

serv_obj = Service(r"F:\python new version\Scripts\chromedriver")
driver = webdriver.Chrome(options=options, service=serv_obj)

# Here we are dealing with authentication, so we need fill multiple input text fields.
# so here we can't provide the required input texts by using find_element method, So
# we have follow the following  syntax:
# driver.get("https://userName:passoward@url")---it's bypass send the details
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

