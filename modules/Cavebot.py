import pyautogui as pg
import time
import threading
import pyautogui as pg
import time
import random
import json
from conf import Constants
from GetLoot import get_loot
from pynput import keyboard
from CheckStatus import check_life, check_mana


def exeta():
    for tecla in Constants.EXETA:
        pg.press(tecla)

def utito():
    for tecla in Constants.UTITO:
        pg.press(tecla)

def kill_box():
            pg.press('9')
            time.sleep(random.uniform(2, 2.1))
            pg.press('8')
            time.sleep(random.uniform(2, 2.7))
            pg.press('9')
            time.sleep(random.uniform(2, 2.4))
            pg.press('0')
            time.sleep(random.uniform(2, 2.8))


def check_battle():
    try:
        pg.locateOnScreen('img/battle_region.png', region=(1572, 24, 154, 51))
        print('Battle vazio')
        return False 
    except pg.ImageNotFoundException:
        print('Monstros encontrados')
        return True

def next_box(path,wait, position):
    # Converte a string "(3750, 166)" para uma tupla (3750, 166)
    position = eval(position)
    
    # Move o mouse para a posição especificada
    pg.moveTo(position[0], position[1])
    pg.sleep(wait)
    pg.click()
    
def check_payer():
    try:
        pg.locateOnScreen('img/player.png', confidence=0.9, region=Constants.MINIMAP)
        print('player encontrado')
        return False 
    except pg.ImageNotFoundException:
        return True

def run():
    with open(f'modules/{Constants.FOLDER_NAME}/infos.json', 'r') as file:
        data = json.loads(file.read())
    for item in data:
        while check_battle() == True:
            print('matando box...')
            kill_box()
            pg.sleep(1)
            get_loot()
            print('Coletando loot')
        next_box(item['path'], item['wait'], item['position'])
        if check_payer() == False:
            kill_box()
            pg.sleep(1)
            get_loot()
            next_box(item['path'], item['wait'], item['position'])


run()