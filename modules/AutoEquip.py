import pyautogui as pg
import time
import random

def check_ring():
    pixel_ring = (1768, 248)
    cor = (71, 74, 77)

    while pg.pixelMatchesColor(*pixel_ring, cor):
        pg.press('j') #hotkey do ring
        time.sleep(random.uniform(0.2, 1))

def check_amulet():
    pixel_amulet = (1769, 179)
    cor = (82, 84, 87)

    while pg.pixelMatchesColor(*pixel_amulet, cor):
        pg.press('k') #hotkey do amuleto
        time.sleep(random.uniform(0.4, 1))