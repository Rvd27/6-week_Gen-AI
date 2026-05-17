import pyautogui
import time
import subprocess

# Step 1: Open Chrome browser
import webbrowser

# Open Google in default browser
webbrowser.open("https://www.google.com")
# Wait for browser to open
time.sleep(3)

# Step 2: Click address bar
pyautogui.hotkey('ctrl', 'l')

# Step 3: Type Google URL
pyautogui.write('https://www.google.com', interval=0.05)

# Press Enter
pyautogui.press('enter')

# Wait for page load
time.sleep(3)

# Step 4: Search for gold price
pyautogui.write('What is the current gold price', interval=0.05)

# Press Enter
pyautogui.press('enter')

print("Automation completed.")