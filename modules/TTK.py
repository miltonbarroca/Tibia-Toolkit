import pyautogui as pg
import time
import threading
import time
import random
import json
import my_thread
import actions
import logging
from conf import Constants
from pynput import keyboard
from pynput.keyboard import Listener

'''
   ▄▄▄▄▀ ▄█ ███   ▄█ ██          ▄▄▄▄▀ ████▄ ████▄ █         █  █▀ ▄█    ▄▄▄▄▀     
▀▀▀ █    ██ █  █  ██ █ █      ▀▀▀ █    █   █ █   █ █         █▄█   ██ ▀▀▀ █        
    █    ██ █ ▀ ▄ ██ █▄▄█         █    █   █ █   █ █         █▀▄   ██     █        
   █     ▐█ █  ▄▀ ▐█ █  █        █     ▀████ ▀████ ███▄      █  █  ▐█    █         
  ▀       ▐ ███    ▐    █       ▀                      ▀       █    ▐   ▀          
                       █                                      ▀                    
                      ▀                                                                                                                              
'''

logging.basicConfig(filename='error.log', level=logging.ERROR)

def kill_box():
    while actions.check_battle():
        if event_th.is_set():
            return
        print('Matando box...')
        pg.press('space')
        pg.press('7')
        pg.press('9')
        if not actions.check_battle() or event_th.is_set() or actions.check_player():
            return
        time.sleep(random.uniform(2, 2.5))
        pg.press('8')
        if not actions.check_battle() or event_th.is_set() or actions.check_player():
            return
        time.sleep(random.uniform(2, 2.5))
        pg.press('9')
        if not actions.check_battle() or event_th.is_set() or actions.check_player():
            return
        time.sleep(random.uniform(2, 2.5))
        pg.press('0')
        pg.press('space')
        pg.press('7')
        if not actions.check_battle() or event_th.is_set() or actions.check_player():
            return
        time.sleep(random.uniform(2, 2.5))

def run():
    try:
        event_th.is_set()
        with open(f'scripts/{Constants.SCRIPT_NAME}.json', 'r') as file:
            data = json.loads(file.read())
        
        while not event_th.is_set():
            for item in data:
                try:
                    if event_th.is_set():
                        return
                    while actions.check_battle():
                        time.sleep(1)
                        pg.press('4')
                        kill_box()
                        if event_th.is_set():
                            return
                        time.sleep(1)
                        actions.get_loot()
                        if event_th.is_set():
                            return
                        actions.check_ring()
                        time.sleep(1)
                        actions.check_amulet()
                        time.sleep(1)
                        pg.press('i')
                        pg.press('s')
                    actions.next_box(item['path'], item['wait'])
                    time.sleep(1)
                    pg.press('i')
                    actions.hole_down(item['down_hole'])
                    if event_th.is_set():
                        return
                    actions.hole_up(item['up_hole'], 'img/stair_up.png', 1, 1)
                    time.sleep(1)
                    pg.press('i')
                    if event_th.is_set():
                        return
                except Exception as e:
                    logging.error(f"Erro durante a execução geral: {e}")
    except Exception as e:
        logging.error(f"Erro durante a execução geral: {e}")

def key_code(key):
    if key == keyboard.Key.esc:
        event_th.set()
        return False
    if key == keyboard.Key.delete:
        event_th.clear()
        if not th_run.is_alive():
            th_run.start()
        start_check_threads()

def check_status(name, delay, x, y, rgb, button_names):
    while not event_th.is_set():
        if not pg.pixelMatchesColor(x, y, rgb):
            for button_name in button_names:
                pg.press(button_name)
                time.sleep(delay)

def start_check_threads():
    global th_check_mana, th_check_life, th_check_exura
    th_check_mana = threading.Thread(target=check_status, args=('mana', 2.1, *Constants.PIXEL_MANA, Constants.COR_MANA, ['3']))
    th_check_life = threading.Thread(target=check_status, args=('life', 1, *Constants.PIXEL_LIFE, Constants.COR_LIFE, ['1']))
    th_check_exura = threading.Thread(target=check_status, args=('exura', 1.9, *Constants.PIXEL_EXURA, Constants.COR_EXURA, ['2']))

    th_check_mana.start()
    th_check_life.start()
    th_check_exura.start()

global event_th
event_th = threading.Event()

th_run = threading.Thread(target=run)

with Listener(on_press=key_code) as listener:
    listener.join()