import pyautogui as pg
from conf import Constants

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
        pg.locateOnScreen('img/battle_player.png', region=Constants.BATTLE_PLAYER)
        print('nenhum player encontrado...')
        return False 
    except pg.ImageNotFoundException:
        print('player encontrado!!!!!!!!!')
        print('parando bot')
        return True
    
def hole_up(shloud_up,img_anchor,plus_x,plus_y):
    if shloud_up:
        box = pg.locateOnScreen(img_anchor, confidence=0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x + plus_x, y + plus_y)
            pg.sleep(1)
            pg.press('F1')
            pg.click()

# keyboard.wait('h')
# hole_up(True,'img/anchor_exotic.png',-80,310)

def hole_down(should_down):
    if should_down:
        box = pg.locateOnScreen('modules/GT_alt/hole_down.png',confidence=0.8)
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

def check_ring():
    if pg.pixelMatchesColor(1769, 277,(36, 39, 42)):
        pg.press('j')
    print('checando ring...')
def check_amulet():
    if pg.pixelMatchesColor(1769, 208,(82, 84, 87)):
        pg.press('k')  
        print('checando amuleto...')
