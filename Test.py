import pyautogui
import time
#Mouse operations
pyautogui.click(100, 100)
time.sleep(2) 
pyautogui.rightClick(100, 100)
time.sleep(4)


pyautogui.click(816,963)
pyautogui.doubleClick(100,100)
pyautogui.dragTo(200,200)
pyautogui.scroll(500)
#keyboard operations
time.sleep(3)
pyautogui.click(743, 960)
time.sleep(2)   
pyautogui.press('enter')    
pyautogui.hotkey('ctrl', 'a')
#image
pyautogui.locateOnScreen('Screenshot 2026-05-16 003806.png')
