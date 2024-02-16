import pyautogui as pg
import time

def check_battle():
    try:
        pg.locateOnScreen('img/battle_region.png', region=(1572, 24, 154, 51))
        return False 
    except pg.ImageNotFoundException:
        return True  

while True:
    have_monster = check_battle()
    print(have_monster)
    time.sleep(1)