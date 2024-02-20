import pyautogui as pg
import time
import random
from conf import Constants


def check_status(name,delay,x,y,rgb,button_name):
    delay = (random.uniform(0.8, 1.2))
    print(f'checando {name}')
    pg.sleep(delay)
    while pg.pixelMatchesColor(x,y,rgb):
        for button_name in button_name:
            pg.press(button_name)

        
check_status('mana',1.2,*Constants.PIXEL_MANA,Constants.COR_MANA,'3')
check_status('life',2,*Constants.PIXEL_LIFE,Constants.COR_LIFE,['1','2'])