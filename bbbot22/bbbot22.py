import pyautogui
from time import sleep
from PIL import Image
from random import *

brother = Image.open('luciano.png')
capt = Image.open('capt.png')
vot =  Image.open('vot_again.png')
h_cap = Image.open('h_cap.png')

comment = 1

mouse_func = [pyautogui.easeOutBack, pyautogui.easeInOutQuad, pyautogui.easeOutQuad, pyautogui.easeInBounce, pyautogui.easeInElastic]


def voto():
    sleep(1)
    w, z = pyautogui.locateCenterOnScreen(capt, confidence=0.8)
    pyautogui.moveTo(w+randint(-20,150), z+randint(-30,10), uniform(0.5, 2.0), choice(mouse_func))
    pyautogui.click()
    sleep(2)
    cap()

def cap():
	if pyautogui.locateCenterOnScreen(h_cap, confidence=0.8) == None:
		a, b = pyautogui.locateCenterOnScreen(vot, confidence=0.8)
		pyautogui.moveTo(a+randint(-250,250), b+randint(-15,15), uniform(0.5, 2.0), choice(mouse_func))
		pyautogui.click()
		sleep(1)
	else:
		pyautogui.press('f5')
		sleep(2)
		irmao()

def irmao():
        pyautogui.scroll(-150)
        sleep(1)
        x, y = pyautogui.locateCenterOnScreen(brother, confidence=0.8)
        pyautogui.moveTo(x+randint(-50,300), y+randint(-5,5), uniform(0.5, 2.0), choice(mouse_func))
        pyautogui.click()
        sleep(1)
        if pyautogui.locateCenterOnScreen(vot, confidence=0.8) == None:
            pyautogui.scroll(-200)
            voto()
        else:
            voto()



while True:
    irmao()
    comment += 1
    print("{} votos computados".format(comment))