import time

import requests
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
from selenium.webdriver.chrome.service import Service
serv_obj = Service(r"F:\python new version\Scripts\chromedriver")
driver = webdriver.Chrome(options=options, service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
All_links =driver.find_elements(By.TAG_NAME, "a")
count = 1

for link in All_links:
    url = link.get_attribute("href")
# Here we try_exception because some network issue b/w client and sever so to avoid this we use this
    try:
        # Make a HEAD request to a web page, and return the HTTP headers and give the status of the code:
        res = requests.head(url)
    except:
        None
    if res.status_code>400:
        print(url , "is the broken link")
        count +=1
    else:
        print(url, " is valid link")
print("The number of the broken links are :", count)
