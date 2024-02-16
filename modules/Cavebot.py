import pyautogui as pg
import time
from AutoCombo import auto_combo, utito, exeta
import threading
import pyautogui as pg
import time
import keyboard
from conf import Constants
#from GetLoot import get_loot

def exeta():
    for tecla in Constants.EXETA:
        pg.press(tecla)

def utito():
    for tecla in Constants.UTITO:
        pg.press(tecla)

def auto_combo():
        exeta()
        for tecla, cooldown in zip(Constants.ATK_SPELLS, Constants.ATK_COOLDOWNS):
            if tecla == '8':
                exeta()
            if tecla == '9':
                utito()
            pg.press(tecla)
            time.sleep(cooldown)
def check_battle():
    try:
        pg.locateOnScreen('img/battle_region.png', region=(1572, 24, 154, 51))
        print('Battle vazio')
        return False 
    except pg.ImageNotFoundException:
        print('Monstros encontrados')
        return True  

have_monster = True

while have_monster:
    have_monster = check_battle()
    if have_monster:
        auto_combo()

    time.sleep(1)