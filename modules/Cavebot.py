import pyautogui as pg
import time
import threading
import pyautogui as pg
import time
import random
import json
import my_thread
import CheckStatus
from conf import Constants
from GetLoot import get_loot
from pynput import keyboard
from pynput.keyboard import Listener


def exeta():
    for tecla in Constants.EXETA:
        pg.press(tecla)

def utito():
    for tecla in Constants.UTITO:
        pg.press(tecla)

def kill_box():
        while check_battle() == True:
            if event_th.is_set():
                return
            pg.press('9')
            time.sleep(random.uniform(2, 2.1))
            if event_th.is_set():
                return
            pg.press('8')
            time.sleep(random.uniform(2, 2.7))
            if event_th.is_set():
                return            
            pg.press('9')
            time.sleep(random.uniform(2, 2.4))
            if event_th.is_set():
                return
            pg.press('0')
            time.sleep(random.uniform(2, 2.8))
            if event_th.is_set():
                return


def check_battle():
    try:
        pg.locateOnScreen('img/battle_region.png', region=(1572, 24, 154, 51))
        print('Battle vazio')
        return False 
    except pg.ImageNotFoundException:
        print('Monstros encontrados')
        return True

def next_box(path,wait, position):
    flag = pg.locateOnScreen(path, confidence= 0.8,region=Constants.MINIMAP)
    if flag:
        position = eval(position)
        if event_th.is_set():
            return
        pg.moveTo(position[0], position[1])
        pg.click()
        pg.sleep(wait)
    
def check_payer():
    try:
        pg.locateOnScreen('img/player.png', confidence=0.9, region=Constants.MINIMAP)
        print('player encontrado')
        return False 
    except pg.ImageNotFoundException:
        return True

def run():
    event_th.is_set()
    with open(f'modules/{Constants.FOLDER_NAME}/infos.json', 'r') as file:
        data = json.loads(file.read())
    while not event_th.is_set():
        for item in data:
            if event_th.is_set():
                return
            while check_battle() == True:
                print('matando box...')
                kill_box()
                if event_th.is_set():
                    return
                pg.sleep(1)
                get_loot()
                if event_th.is_set():
                    return
                print('Coletando loot')
            next_box(item['path'], item['wait'], item['position'])
            if event_th.is_set():
                return
            if check_payer() == False:
                kill_box()
                if event_th.is_set():
                    return
                pg.sleep(1)
                get_loot()
                if event_th.is_set():
                    return
                next_box(item['path'], item['wait'], item['position'])
                if event_th.is_set():
                    return


def key_code(key,th_group):
    if key == keyboard.Key.esc:
        event_th.set()
        th_group.stop()
        return False
    if key == keyboard.Key.delete:
        th_group.start()
        th_run.start()

global event_th
event_th = threading.Event()
th_run = threading.Thread(target=run)

th_check_mana = my_thread.MyThread(lambda : CheckStatus.check_status('mana',1,*Constants.PIXEL_MANA,Constants.COR_MANA,'3'))
th_check_life = my_thread.MyThread(lambda : CheckStatus.check_status('life',2,*Constants.PIXEL_LIFE,Constants.COR_LIFE,'1'))

group_threads = my_thread.ThreadGroup([th_check_mana,th_check_life])

with Listener(on_press=lambda key: key_code(key, group_threads)) as listener :
    listener.join()
