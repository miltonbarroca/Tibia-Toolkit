import pyautogui as pg
import time
import keyboard

def check_ring():
    if pg.pixelMatchesColor(1768, 248,(71, 74, 77)):
        pg.press('j')
    print('checando ring...')
def check_amulet():
    if pg.pixelMatchesColor(1769, 180,(82, 84, 87)):
        pg.press('k')  
        print('checando amuleto...')