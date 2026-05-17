import pyautogui
import time
import subprocess

# -----------------------------------
# STEP 1 : Open Chrome Browser
# -----------------------------------

subprocess.Popen(r"C:\Users\HP\AppData\Local\Google\Chrome\Application\chrome.exe"
)

# Wait for browser to open
time.sleep(3)

# -----------------------------------
# STEP 2 : Focus Address Bar
# -----------------------------------

pyautogui.hotkey('ctrl', 'l')

# -----------------------------------
# STEP 3 : Open Google
# -----------------------------------

pyautogui.write('https://www.google.com', interval=0.05)

pyautogui.press('enter')

# Wait for page load
time.sleep(4)

# -----------------------------------
# STEP 4 : Search IPL Score
# -----------------------------------

pyautogui.write(
    'CSK vs Lucknow score IPL 2026',
    interval=0.05
)

pyautogui.press('enter')

# Wait for results
time.sleep(5)

# -----------------------------------
# STEP 5 : Click First Search Result
# -----------------------------------

# Press TAB few times to reach results
pyautogui.press('tab', presses=5, interval=0.5)

# Press ENTER to open first result
pyautogui.press('enter')

print("Automation completed successfully.")