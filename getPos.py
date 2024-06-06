import pyautogui
import time

# time.sleep(2)
# pyautogui.vscroll(-3000)


try:
    while True:
        x,y = pyautogui.position()
        print(f"pyautogui.moveTo( x = {x}, y= {y}, duration = x)")
        time.sleep(2)
except KeyboardInterrupt:
    print('Abgebrochen')
