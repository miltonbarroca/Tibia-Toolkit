import pyautogui as pg
import time
import threading
import pyautogui as pg
import time
import random
from conf import Constants
from GetLoot import get_loot
from pynput import keyboard
from CheckStatus import check_life, check_mana

def exeta():
    for tecla in Constants.EXETA:
        pg.press(tecla)

def utito():
    for tecla in Constants.UTITO:
        pg.press(tecla)

def kill_box():
            pg.press('9')
            time.sleep(random.uniform(2, 2.1))
            pg.press('8')
            time.sleep(random.uniform(2, 2.7))
            pg.press('9')
            time.sleep(random.uniform(2, 2.4))
            pg.press('0')
            time.sleep(random.uniform(2, 2.8))


def check_battle():
    try:
        pg.locateOnScreen('img/battle_region.png', region=(1572, 24, 154, 51))
        print('Battle vazio')
        return False 
    except pg.ImageNotFoundException:
        print('Monstros encontrados')
        return True

def run():
        while True:
            if check_battle() == True:
                kill_box()
            get_loot()
            print('Coletando loot')
            time.sleep(1)

run()