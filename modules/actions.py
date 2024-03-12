import pyautogui as pg
from conf import Constants
import keyboard

def check_battle():
    try:
        pg.locateOnScreen('img/battle_region.png', region=Constants.BATTLE_REGION)
        print('Battle vazio,indo para proxima box...')
        return False 
    except pg.ImageNotFoundException:
        print('Monstros encontrados')
        return True
    

def check_player():
    try:
        pg.locateOnScreen('img/player.png', confidence=0.9, region=Constants.MINIMAP)
        print('player encontrado')
        return False 
    except pg.ImageNotFoundException:
        return True
    
def hole_up(img_anchor,plus_x,plus_y):
    box = pg.locateOnScreen(img_anchor, confidence=0.8)
    if box:
        x, y = pg.center(box)
        pg.moveTo(x + plus_x, y + plus_y)
        pg.press('F1')
        pg.click()

#hole_up('img/anchor_GT_alt_up.png',270,130)

def hole_down(should_down):
    if should_down:
        box = pg.locateOnScreen('img/hole_GT_alt.png',confidence=0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x,y)
            pg.click()
            pg.sleep(3)

def next_box(path,wait):
    flag = pg.locateOnScreen(path, confidence= 0.9,region=Constants.MINIMAP)
    if flag:
        x,y = pg.center(flag)
        pg.moveTo(x,y)
        pg.click()
        pg.sleep(wait)

loot_coordinates = [
    (2849, 478),
    (2907, 479),
    (2914, 545),
    (2911, 613),
    (2843, 613),
    (2771, 607),
    (2772, 539),
    (2771, 477)
]

def get_loot():
    print('Coletando loot...')
    keyboard.press('shift')
    for coord in loot_coordinates:
        pg.click(x=coord[0], y=coord[1], button='right')
    keyboard.release('shift')



