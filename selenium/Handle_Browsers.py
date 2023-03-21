import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
serv_obj = Service(r"C:\pythonProject\venv\Scripts\chromedriver")
driver = webdriver.Chrome(options=options, service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/") # 1st window, And title = Automation Testing Practice
driver.maximize_window()
driver.implicitly_wait(10)
Input_box = driver.find_element(By.CSS_SELECTOR, "input.wikipedia-search-input")
Input_box.send_keys("selenium")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, ".wikipedia-search-button").click()

driver.switch_to.new_window() # 2nd window
driver.get('https://www.google.com/' )
ib = driver.find_element(By.NAME, "q")
ib.send_keys("python")
ib.send_keys(Keys.ENTER)
for i in range(2):
    driver.switch_to.new_window()
    if i == 0:
        win3 = driver.get('https://www.facebook.com/') # win3
    elif i == 1:
        driver.get('https://www.flipkart.com/') # win4
        time.sleep(3)
        driver.find_element(By.XPATH, '//button[@class ="_2KpZ6l _2doB4z"]').click()



wins = driver.window_handles  #  To get open windows id's we have to use this
# Here we need to understand these IDs are generate dynamically, so we need to use index concept
print(wins)
for win in wins:
    driver.switch_to.window(win)
    print(driver.title)
    if driver.title ==  "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!":
        driver.close()
    elif driver.title == "Facebook – log in or sign up":
        driver.close()
driver.quit()