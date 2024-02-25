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
    
def hole_up(should_up):
    if should_up:
        try:
            box = pg.locateOnScreen('img/anchor_GT.png', confidence=0.8)
            if box:
                x, y = pg.center(box)
                pg.moveTo(2779, 614)
                pg.press('F1')
                pg.click()
                pg.sleep(3)
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            pass

def hole_down(should_down):
    if should_down:
        try:
            box = pg.locateOnScreen('img/hole_down.png', confidence=0.8)
            if box:
                x, y = pg.center(box)
                pg.moveTo(2780, 349)
                pg.click()
                pg.sleep(5)
        except Exception as e:
            pass

def next_box(path,wait, position):
    flag = pg.locateOnScreen(path, confidence= 0.8,region=Constants.MINIMAP)
    if flag:
        position = eval(position)
        pg.moveTo(position[0], position[1])
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
    keyboard.press('shift')
    for coord in loot_coordinates:
        pg.click(x=coord[0], y=coord[1], button='right')
    keyboard.release('shift')



