import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

srv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")
driver = webdriver.Chrome(service=srv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

title_of_Table = driver.find_element(By.XPATH,"//h2[contains(text(),'HTML Table')]")
No_Of_Ttable_headers = driver.find_elements(By.XPATH, "//div//th")

print('The title of the table is :', title_of_Table.text)
print("Total no of the headers of table is =", len(No_Of_Ttable_headers))

for i in range(1,len(No_Of_Ttable_headers)+1):
    header = driver.find_element(By.XPATH, "//div//th["+str(i)+"]") # Here pass values in xpath dynamically  we need to use this
    print('The header of {} is :'.format(i), header.text)
print("-----------------------------------------------------")
print()
rows = driver.find_elements(By.XPATH, '//div/table[@name="BookTable"]//tbody//tr')
coloumns = driver.find_elements(By.XPATH, '//div/table[@name="BookTable"]//tbody//tr//th')
print("No of the Rows is :", len(rows))
for j in range(1, len(rows)+1):
    rs = driver.find_element(By.XPATH, "//div/table[@name='BookTable']//tbody//tr["+str(j)+"]")

    print('The Row No.{} is :'.format(j), rs.text)
print("---------------------------------------------------------")
print()
print("No of the cols is :", len(coloumns))
for j in range(1, len(coloumns)+1):
    c1 = driver.find_element(By.XPATH, "//div/table[@name='BookTable']//tbody//tr//th["+str(j)+"]")

    print('The Coloumns No.{} is :'.format(j), c1.text,)


print()
driver.execute_script()


time.sleep(5)

