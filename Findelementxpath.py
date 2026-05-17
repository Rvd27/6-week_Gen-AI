from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.google.com")

# Locate Google search box using XPath
search_box = driver.find_element(
    By.XPATH,
    "//textarea[@name='q']"
)

# Type query
search_box.send_keys("Pak vs Bangladesh Test Match")

# Press Enter
search_box.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()