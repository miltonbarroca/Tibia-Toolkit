import pyautogui as pg
import time
import random
from conf import Constants


def check_status(name,delay,x,y,rgb,button_name):
    print(f'checando {name}')
    pg.sleep(1)
    while pg.pixelMatchesColor(x,y,rgb):
        for button_name in button_name:
            pg.press(button_name)
