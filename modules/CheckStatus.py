import pyautogui as pg
import time
import random

def check_mana():
    pixel_mana = (965, 33)
    cor = (36, 36, 36)

    while pg.pixelMatchesColor(*pixel_mana, cor):
        pg.press('3')
        time.sleep(random.uniform(0.8, 1.2))
        
def check_life():
    pixel_life = (1853, 308)
    cor = (69, 82, 109)

    while pg.pixelMatchesColor(*pixel_life, cor):
        pg.press('2')
        time.sleep(random.uniform(0.4, 0.6))  
        pg.press('1')  # hotkey de cura
        time.sleep(random.uniform(0.8, 1.2))
