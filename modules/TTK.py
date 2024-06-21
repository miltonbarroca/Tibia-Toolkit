import pyautogui as pg
import time
import threading
import time
import random
import json
import my_thread
import actions
import logging
import CheckStatus
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
        pg.press('3')
        pg.press('2')
        if not actions.check_battle() or event_th.is_set() or actions.check_player():
            return
        time.sleep(random.uniform(2, 2.5))
        pg.press('3')
        pg.press('8')
        pg.press('3')
        pg.press('2')
        if not actions.check_battle() or event_th.is_set() or actions.check_player():
            return
        time.sleep(random.uniform(2, 2.5))
        pg.press('3')
        pg.press('9')
        pg.press('3')
        pg.press('2')
        if not actions.check_battle() or event_th.is_set() or actions.check_player():
            return
        time.sleep(random.uniform(2, 2.5))
        pg.press('3')
        pg.press('0')
        pg.press('3')
        pg.press('2')
        pg.press('space')
        pg.press('3')
        pg.press('7')
        pg.press('3')
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
                        pg.sleep(1)
                        pg.press('4')
                        kill_box()
                        if event_th.is_set():
                            return
                        pg.sleep(1)
                        actions.get_loot()
                        if event_th.is_set():
                            return
                        actions.check_ring()
                        pg.sleep(1)
                        actions.check_amulet()
                        pg.sleep(1)
                        pg.press('i')
                    actions.next_box(item['path'], item['wait'])
                    pg.sleep(1)    
                    pg.press('i')
                    actions.hole_down(item['down_hole'])
                    if event_th.is_set():
                        return
                    actions.hole_up(item['up_hole'],'img/stair_up.png',1,1)
                    pg.sleep(1)
                    pg.press('i')
                    if event_th.is_set():
                        return
                except Exception as e:
                    logging.error(f"Erro durante a execução geral: {e}")
    except Exception as e:
        logging.error(f"Erro durante a execução geral: {e}")

def key_code(key,th_group): #key_code(key, th_group)
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
thread_hp = threading.Thread(lambda:CheckStatus.check_status, args=('HP', 1, '1'))
thread_mp = threading.Thread(lambda:CheckStatus.check_status, args=('MP', 2.2, '3'))


group_threads = my_thread.ThreadGroup([thread_hp,thread_mp])

with Listener(on_press=lambda key: key_code(key,group_threads)) as listener :
    listener.join()