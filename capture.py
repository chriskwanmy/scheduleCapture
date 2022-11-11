import pyautogui
from datetime import datetime
import pygetwindow as gw
import time
time.sleep(1)
datenow = datetime.now().strftime("%Y%m%d")
filename = datenow+".jpg"
cmd = gw.getWindowsWithTitle("C:\\Users\\chris\\anaconda3\\python.exe")[0]
cmd.minimize()

time.sleep(2)
pyautogui.screenshot(filename)

time.sleep(5)
pyautogui.keyDown('winleft')
pyautogui.keyDown('d')
pyautogui.keyUp('d')
pyautogui.keyUp('winleft')

print("finished")