import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
srv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")


driver = webdriver.Chrome(service=srv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

rows = driver.find_elements(By.XPATH,'//table [@name = "BookTable"]//tr')
print(len(rows))
# To print the data in tabular format
#for r in range(2, len(rows)):
#    for c in range(1,5):
#        data = driver.find_element(By.XPATH,'//table [@name = "BookTable"]//tr['+str(r)+']/td['+str(c)+']').text
#        print(data, end="                 ")
#    print()

# read data based on condition(List books name whose author is Mukesh)
for r in range(2, len(rows)):
    authorName = driver.find_element(By.XPATH,'//table [@name = "BookTable"]//tr['+str(r)+']/td[2]').text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH,'//table [@name = "BookTable"]//tr['+str(r)+']/td[1]').text
        print(bookName, "      ", authorName)


