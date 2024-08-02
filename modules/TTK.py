import pyautogui as pg
import time
import threading
import time
import random
import json
import my_thread
import actions
import logging
from checkstatus import *
from conf import Constants
from pynput import keyboard
from pynput.keyboard import Listener
import pygame

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


ALARM_SOUND = 'sound\evacuation_alarm.wav'

def play_alarm():
    """Função para tocar o alarme."""
    pygame.mixer.init()
    pygame.mixer.music.load(ALARM_SOUND)
    pygame.mixer.music.play()

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

def run(event_th):
    try:
        with open(f'scripts/{Constants.SCRIPT_NAME}.json', 'r') as file:
            data = json.loads(file.read())
        
        while not event_th.is_set():
            if actions.check_player():
                print("Player detected. Stopping bot execution and playing alarm.")
                play_alarm()  # Toca o alarme
                event_th.set()  # Para a execução do bot
                return
            for item in data:
                try:
                    if event_th.is_set() or actions.check_player():
                        return
                    while actions.check_battle():
                        pg.sleep(1)
                        pg.press('4')
                        kill_box()
                        if event_th.is_set() or actions.check_player():
                            return
                        pg.sleep(1)
                        pg.press('l')
                        if event_th.is_set() or actions.check_player():
                            return
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

def key_code(key):
    global th_suplies, th_run, event_suplies, event_th

    if key == keyboard.Key.esc:
        event_th.set()
        event_suplies.set()
        th_suplies.join()
        th_run.join()
        return False

    if key == keyboard.Key.delete:
        event_suplies.clear()
        event_th.clear()
        th_suplies = threading.Thread(target=manager_suplies, args=(event_suplies,))
        th_run = threading.Thread(target=run, args=(event_th,))
        th_suplies.start()
        th_run.start()

event_suplies = threading.Event()
event_th = threading.Event()
th_suplies = threading.Thread(target=manager_suplies, args=(event_suplies,))
th_run = threading.Thread(target=run, args=(event_th,))

with Listener(on_press=lambda key: key_code(key)) as listener:
    listener.join()