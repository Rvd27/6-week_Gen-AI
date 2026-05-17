from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Open login page
driver.get("https://the-internet.herokuapp.com/login")

# Browser navigation
driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

# Find username textbox
username = driver.find_element(By.ID, "username")

# Interactions
username.click()

username.send_keys("Rahul")

time.sleep(2)

username.clear()

# Screenshot
driver.save_screenshot("screenshot.png")

print("Screenshot saved successfully")

time.sleep(3)

driver.quit()