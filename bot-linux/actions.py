import pyautogui as pg
from conf import Constants
import os
import random
import asyncio
from telegramsend import send_message

def check_battle():
    try:
        pg.locateOnScreen('imgs/battle_region.png', confidence=0.8, region=Constants.BATTLE_REGION)
        print('Battle vazio, indo para proxima box...')
        return False
    except pg.ImageNotFoundException:
        print('Monstros encontrados')
        return True

def check_player():
    try:
        pg.locateOnScreen('imgs/battle_player.png', confidence=0.8, region=Constants.BATTLE_PLAYER)
        print('nenhum player encontrado...')
        return False
    except pg.ImageNotFoundException:
        print('player encontrado!!!!!!!!!!!!!!!!!!!!!!!')
        asyncio.run(send_message(text='Player na hunt !!!', chat_id=Constants.CHAT_ID))
        return True

def check_player_position():
    try:
        pg.locateOnScreen('imgs/player.png', confidence=0.8, region=Constants.MINIMAP)
        print('nao chego no waypoint...')
        return True
    except pg.ImageNotFoundException:
        print('chegou no waypoint...')
        return False

def next_box(path,wait):
    try:
        flag = pg.locateOnScreen(path, confidence=0.7, region=Constants.MINIMAP)
        if flag:
            x,y = pg.center(flag)
            pg.moveTo(x,y)
            pg.click()
            pg.sleep(wait)

    except pg.ImageNotFoundException:
        print('ImageNotFoundException: image not found')


loot_coordinates = [
    (491, 336),
    (495, 376),
    (503, 419),
    (550, 419),
    (595, 416),
    (595, 378),
    (599, 337),
    (549, 336)
]

def get_loot():
    print('Coletando loot...')
    random.shuffle(loot_coordinates)
    pg.keyDown('shift')
    for coord in loot_coordinates:
        pg.click(x=coord[0], y=coord[1], button='right')
    pg.keyUp('shift')

def check_amulet():
    if pg.pixelMatchesColor(1769, 208,(82, 84, 87)):
        pg.press('k')
        print('checando amuleto...')

def check_ring():
    try:
        pg.locateOnScreen('imgs/ring_region.png', confidence=0.8, region=Constants.RING_REGION)
        print('ring vazio...')
        return False
    except pg.ImageNotFoundException:
        print('ring sendo utilizado...')
        return True
