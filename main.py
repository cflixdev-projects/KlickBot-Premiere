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

def start():
    x = 0.5
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

    # kreativ - scharf, dnymaik, sättigung
    pyautogui.moveTo(x=1318, y=549, duration=x)
    pyautogui.click()
    pyautogui.write('4')

    pyautogui.moveTo(x=1321, y=584, duration=x)
    pyautogui.click()
    pyautogui.write('8')

    pyautogui.moveTo(x=1325, y=613, duration=x)
    pyautogui.click()
    pyautogui.write('104')
    pyautogui.press('enter')

    pyautogui.scroll(5000)

    pyautogui.moveTo( x = 643, y= 359,duration=x)
    pyautogui.click()
    pyautogui.moveTo(y= 610,duration=x)


    pyautogui.mouseDown(button='left', x=880, y=465,)
    # runter bringen
    pyautogui.moveTo(x=880, y=798,)
    # lösen

    pyautogui.mouseUp(button='left', x=880, y=798)

    '''
    dialog vorgabe muss leer sein
    darf nichts vorher ausgewhlt sein, also sprache verbessern oder sonst draufgeklickt worden sein
    mit esc schließen
    '''

    # audio

    # essential sound
    pyautogui.moveTo(x=955, y=116, duration=x)
    pyautogui.click()
    #vorgabe
    pyautogui.moveTo(x=868, y=240, duration=x)
    pyautogui.click()
    # move to dialog
    pyautogui.moveTo(x=625, y=262, duration=x)
    pyautogui.click()
    # dialog -> dialog mit rauschen
    pyautogui.moveTo(x=783, y=422, duration=x)
    pyautogui.click()

    # sprache verbessern
    pyautogui.moveTo(x=489, y=331, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=489, y=371, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=1330, y=405, duration=x)
    pyautogui.click()
    pyautogui.write('3,5')
    pyautogui.press('enter')

    # reparieren
    pyautogui.moveTo(x=489, y=331, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=503, y=428, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=1333, y=478, duration=x)
    pyautogui.click()
    pyautogui.write('3,5')
    pyautogui.press('enter')

    # rumpeln und dehum
    # reparieren muss offen sein
    # geht mit maus nach links wohinmach scrollen kann
    scroll(-3000)

    pyautogui.moveTo(x=1326, y=341, duration=x)
    pyautogui.click()
    pyautogui.write('4')
    pyautogui.press('enter')

    pyautogui.moveTo(x=449, y=423, duration=x)
    pyautogui.click()

    pyautogui.moveTo(x=1331, y=420, duration=x)
    pyautogui.click()
    pyautogui.write('3,3')
    pyautogui.press('enter')


    scroll(-3000)
    # de ess
    pyautogui.moveTo(x=1326, y=325, duration=x)
    pyautogui.click()
    pyautogui.write('3,8')

    pyautogui.moveTo( x = 458, y= 396, duration = x)
    pyautogui.click()
    pyautogui.moveTo( x = 1326, y= 389, duration = x)
    pyautogui.click()
    pyautogui.write('3')
    pyautogui.press('enter')

    # klarkheit tiefe tonlage
    scroll(-3000)
    pyautogui.moveTo(x=1326, y=440, duration=x)
    pyautogui.click()
    pyautogui.moveTo( x = 1081, y= 438, duration = x)
    pyautogui.click()

    pyautogui.moveTo( x = 458, y= 483, duration = x)
    pyautogui.click()
    pyautogui.moveTo(x=1320, y=482, duration=x)
    pyautogui.click()
    pyautogui.write('3,5')
    pyautogui.press('enter')
    scroll(-3000)
    #klarheit
    pyautogui.moveTo(x=448, y=434, duration=x)
    pyautogui.click()

    pyautogui.moveTo(x=568, y=469, duration=x)
    pyautogui.click()

    pyautogui.moveTo(x=581, y=655, duration=x)
    pyautogui.click()
    scroll(-3000)
    #stimmlage
    pyautogui.moveTo( x = 451, y= 479, duration = x)
    pyautogui.click()
    pyautogui.moveTo( x = 630, y= 510, duration = x)
    pyautogui.click()

    scroll(-3000)

    # klarheit
    pyautogui.moveTo(x=1330, y=496, duration=x)
    pyautogui.click()
    pyautogui.moveTo( x = 559, y= 493, duration = x)
    pyautogui.click()
    scroll(-3000)

    pyautogui.moveTo(x=544, y=404, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=554, y=630, duration=x)
    pyautogui.click()
    pyautogui.moveTo(x=1297, y=459, duration=x)
    pyautogui.click()
    pyautogui.write('2,5')
    pyautogui.press('enter')


'''
    effekte = umschalt + 7 damit das effekt fenster/arbeitsbereich sich links öffnet
    '''


if __name__ == '__main__':

    screen_width, screen_height = pyautogui.size()

    print("Screen width:", screen_width)
    print("Screen height:", screen_height)
    start()