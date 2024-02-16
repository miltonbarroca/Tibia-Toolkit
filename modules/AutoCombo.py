import pyautogui as pg
import time
import keyboard
from conf import Constants

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
