import pyautogui
import time
import keyboard

'''
1920 x 1080
my laptop
bei angeschlossenen bildschirmen könne probleme auftreten
Arbeitsbereiche - Vertikal
nicht die fenster verschieben, größer/kleine machen
Clip auswählen

zuerst lumetri farben
muss einfache korrektur angeklickt sein
eingabe lut
709ee 
test
'''
if __name__ == '__main__':

    screen_width, screen_height = pyautogui.size()

    print("Screen width:", screen_width)
    print("Screen height:", screen_height)

# try:
#     while True:
#         x,y = pyautogui.position()
#         print(f"pyautogui.moveTo( x = {x}, y= {y},)")
#         time.sleep(2)
# except KeyboardInterrupt:
#     print('Abgebrochen')
#


def start():
    time.sleep(3)
    # move to lumtri farben
    pyautogui.moveTo(x=641, y=115, )
    pyautogui.click()
    # click lut
    pyautogui.moveTo(x=633, y=308,)
    pyautogui.click()
    # choose lut
    pyautogui.moveTo(x=690, y=471,)
    pyautogui.click()
    # klick automatic
    pyautogui.moveTo(x = 1176, y= 357,)
    pyautogui.click()
    time.sleep(1)
    # move to scroll bar, scroll down
    pyautogui.mouseDown(button='left', x=1372, y=322,)
    # runter bringen
    pyautogui.moveTo(x=1372, y=565,)
    # lösen
    pyautogui.mouseUp(button='left', x=1372, y=565)

    # klick kreativ
    pyautogui.moveTo(x=472, y=426, )
    pyautogui.click()
    #
    # # kreativ - scharf, dnymaik, sättigung
    # pyautogui.moveTo(x=1318, y=549, )
    # pyautogui.click()
    # pyautogui.write('4')
    #
    # pyautogui.moveTo(x=1321, y=584, )
    # pyautogui.click()
    # pyautogui.write('8')
    #
    # pyautogui.moveTo(x=1325, y=613, )
    # pyautogui.click()
    # pyautogui.write('104')
    # pyautogui.press('enter')
    #
    # pyautogui.vscroll(5000)
    #
    # pyautogui.moveTo( x = 643, y= 359,)
    # pyautogui.click()
    # pyautogui.moveTo(y= 610,)
    #
    #
    # pyautogui.mouseDown(button='left', x=880, y=465,)
    # # runter bringen
    # pyautogui.moveTo(x=880, y=798,)
    # # lösen
    # pyautogui.mouseUp(button='left', x=880, y=798)
    # pyautogui.moveTo(x=569, y=570, )
    # pyautogui.click()
