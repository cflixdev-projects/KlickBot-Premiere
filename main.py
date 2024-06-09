import os
import sys
import multiprocessing
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


# try:
#     while True:
#         x,y = pyautogui.position()
#         print(f"pyautogui.moveTo( x = {x}, y= {y},)")
#         time.sleep(2)
# except KeyboardInterrupt:
#     print('Abgebrochen')
#


def scroll(sValue):
    x = 0.5
    pyautogui.moveTo(x=424, y=465, duration=x)

    pyautogui.scroll(sValue)


offset_x = 0
offset_y = 0
def start(offset_x, offset_y):

    x = 0.5
    time.sleep(3)
    # move to lumtri farben
    pyautogui.moveTo(x=641 + offset_x, y=115 + offset_y, )
    pyautogui.click()
    # click lut
    pyautogui.moveTo(x=633+ offset_x, y=308+ offset_y,)
    pyautogui.click()
    # choose lut
    pyautogui.moveTo(x=690+ offset_x, y=471+ offset_y,)
    pyautogui.click()
    # klick automatic
    pyautogui.moveTo(x = 1176+ offset_x, y= 357+ offset_y,)
    pyautogui.click()
    time.sleep(1)
    # move to scroll bar, scroll down
    pyautogui.mouseDown(button='left', x=1372, y=322+ offset_y,)
    # runter bringen
    pyautogui.moveTo(x=1372+ offset_x, y=565+ offset_y,)
    # lösen
    pyautogui.mouseUp(button='left', x=1372+ offset_x, y=565+ offset_y)

    # klick kreativ
    pyautogui.moveTo(x=472+ offset_x, y=426, )
    pyautogui.click()

    # kreativ - scharf, dnymaik, sättigung
    pyautogui.moveTo(x=1318+ offset_x, y=549+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.write('4')

    pyautogui.moveTo(x=1321+ offset_x, y=584+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.write('8')

    pyautogui.moveTo(x=1325+ offset_x, y=613+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.write('104')
    pyautogui.press('enter')

    pyautogui.scroll(5000)

    pyautogui.moveTo( x = 643+ offset_x, y= 359+ offset_y,duration=x)
    pyautogui.click()
    pyautogui.moveTo(y= 610+ offset_y,duration=x)


    pyautogui.mouseDown(button='left', x=880+ offset_x, y=465+ offset_y,)
    # runter bringen
    pyautogui.moveTo(x=880+ offset_x, y=798+ offset_y,)
    # lösen

    pyautogui.mouseUp(button='left', x=880+ offset_x, y=798+ offset_y)

    '''
    dialog vorgabe muss leer sein
    darf nichts vorher ausgewhlt sein, also sprache verbessern oder sonst draufgeklickt worden sein
    mit esc schließen
    '''

    # audio

    # essential sound
    pyautogui.moveTo(x=955+ offset_x, y=116+ offset_y, duration=x)
    pyautogui.click()
    #vorgabe
    pyautogui.moveTo(x=868+ offset_x, y=240+ offset_y, duration=x)
    pyautogui.click()
    # move to dialog
    pyautogui.moveTo(x=625+ offset_x, y=262+ offset_y, duration=x)
    pyautogui.click()
    # dialog -> dialog mit rauschen
    pyautogui.moveTo(x=783+ offset_x, y=422+ offset_y, duration=x)
    pyautogui.click()

    # sprache verbessern
    pyautogui.moveTo(x=489+ offset_x, y=331+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=489+ offset_x, y=371+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=1330+ offset_x, y=405+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.write('3,5')
    pyautogui.press('enter')

    # reparieren
    pyautogui.moveTo(x=489+ offset_x, y=331  + offset_y, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=503+ offset_x, y=428+ offset_y , duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=1333+ offset_x, y=478+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.write('3,5')
    pyautogui.press('enter')

    # rumpeln und dehum
    # reparieren muss offen sein
    # geht mit maus nach links wohinmach scrollen kann
    scroll(-3000)

    pyautogui.moveTo(x=1326+ offset_x, y=341+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.write('4')
    pyautogui.press('enter')

    pyautogui.moveTo(x=449+ offset_x, y=423+ offset_y, duration=x)
    pyautogui.click()

    pyautogui.moveTo(x=1331+ offset_x, y=420+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.write('3,3')
    pyautogui.press('enter')


    scroll(-3000)
    # de ess
    pyautogui.moveTo(x=1326+ offset_x, y=325+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.write('3,8')

    pyautogui.moveTo( x = 458+ offset_x, y= 396+ offset_y, duration = x)
    pyautogui.click()
    pyautogui.moveTo( x = 1326+ offset_x, y= 389+ offset_y, duration = x)
    pyautogui.click()
    pyautogui.write('3')
    pyautogui.press('enter')

    # klarkheit tiefe tonlage
    scroll(-3000)
    pyautogui.moveTo(x=1326+ offset_x, y=440+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.moveTo( x = 1081+ offset_x, y= 438+ offset_y, duration = x)
    pyautogui.click()

    pyautogui.moveTo( x = 458+ offset_x, y= 483+ offset_y, duration = x)
    pyautogui.click()
    pyautogui.moveTo(x=1320+ offset_x, y=482+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.write('3,5')
    pyautogui.press('enter')
    scroll(-3000)
    #klarheit
    pyautogui.moveTo(x=448+ offset_x, y=434+ offset_y, duration=x)
    pyautogui.click()

    pyautogui.moveTo(x=568+ offset_x, y=469+ offset_y, duration=x)
    pyautogui.click()

    pyautogui.moveTo(x=581+ offset_x, y=655+ offset_y, duration=x)
    pyautogui.click()
    scroll(-3000)
    #stimmlage
    pyautogui.moveTo( x = 451+ offset_x, y= 479+ offset_y, duration = x)
    pyautogui.click()
    pyautogui.moveTo( x = 630+ offset_x, y= 510+ offset_y, duration = x)
    pyautogui.click()

    scroll(-3000)

    # klarheit
    pyautogui.moveTo(x=1330+ offset_x, y=496+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.moveTo( x = 559+ offset_x, y= 493+ offset_y, duration = x)
    pyautogui.click()
    scroll(-3000)

    pyautogui.moveTo(x=544+ offset_x, y=404+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=554+ offset_x, y=630+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=1297+ offset_x, y=459+ offset_y, duration=x)
    pyautogui.click()
    pyautogui.write('2,5')
    pyautogui.press('enter')

'''k
    effekte = umschalt + 7 damit das effekt fenster/arbeitsbereich sich links öffnet
    '''


# multiprocessing


# p2 = multiprocessing.Process(target=start)


if __name__ == '__main__':


    screen_width, screen_height = pyautogui.size()


    print("Screen width:", screen_width)
    print("Screen height:", screen_height)
    start(offset_x,offset_y)
    # p1.start()
    # p2.start()


    # p1.join()
    # p2.join()

# finish  = time.perf_counter()
# print("Finished running after seconds : ", finish)
#



