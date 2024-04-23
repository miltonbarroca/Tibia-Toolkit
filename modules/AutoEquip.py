import pyautogui as pg
import time

def check_ring():
    if pg.pixelMatchesColor(1769, 277,(36, 39, 42)):
        pg.press('j')
    print('checando ring...')
def check_amulet():
    if pg.pixelMatchesColor(1769, 208,(82, 84, 87)):
        pg.press('k')  
        print('checando amuleto...')