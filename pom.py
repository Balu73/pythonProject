from selenium import webdriver
from LoginTest import LoginPage
import time
# Create a new instance of the web driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

# Create an instance of the LoginPage class
login_page = LoginPage(driver)

# Enter the username and password
login_page.enter_username("student")
login_page.enter_password("Possword123")

# Click the login button
login_page.click_login_button()

# Assert that the user is logged in
assert driver.current_url == "https://practicetestautomation.com/practice-test-login/"

# Close the browser
driver.quit()
