import pyautogui as pg
import time
import threading
import pyautogui as pg
import time
import keyboard
from conf import Constants
from GetLoot import get_loot
import random

def exeta():
    for tecla in Constants.EXETA:
        pg.press(tecla)

def utito():
    for tecla in Constants.UTITO:
        pg.press(tecla)

def combo():
            pg.press('9')
            time.sleep(random.uniform(2, 2.4))

            pg.press('8')
            time.sleep(random.uniform(2, 2.4))

            pg.press('9')
            time.sleep(random.uniform(2, 2.4))

            pg.press('0')
            time.sleep(random.uniform(2, 2.4))


def check_battle():
    try:
        pg.locateOnScreen('img/battle_region.png', region=(1572, 24, 154, 51))
        print('Battle vazio')
        return False 
    except pg.ImageNotFoundException:
        print('Monstros encontrados')
        return True  


have_monster = True

def run():
    global have_monster
    while have_monster:
        have_monster = check_battle()
        if have_monster:
            combo()
            time.sleep(1)
            get_loot()
            print('Coletando loot')
        time.sleep(1)

