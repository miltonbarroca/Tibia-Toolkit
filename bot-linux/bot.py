import pyautogui as pg
import time
import actions
import json
import random
import pynput
import os
from conf import Constants
from threading import Thread, Event

# force use of ImageNotFoundException
pg.useImageNotFoundException()
pg.FAILSAFE = False

def monitor_status():
    while not event_th.is_set():
        actions.check_life('F1', 'F3')
        time.sleep(0.2)
        actions.check_mana('F2')
        time.sleep(0.2)
        actions.check_food('f')
        time.sleep(0.2)
        actions.check_ring('f11')
        time.sleep(0.2)
        actions.check_follow()
        time.sleep(0.2)

def bot():
    while not event_th.is_set():
        with open(f'scripts/{Constants.SCRIPT_NAME}.json', 'r') as file:
            data = json.loads(file.read())
            if event_th.is_set():
                return
            for item in data:
                actions.next_box(item['path'], item['wait'])
                if event_th.is_set():
                    return
                while actions.check_battle():
                    if event_th.is_set():
                        return
                    pg.press('=')
                    time.sleep(5)
                    pg.press('l')

def start_bot():
    global th_bot, thread_status
    th_bot = Thread(target=bot)
    thread_status = Thread(target=monitor_status)
    th_bot.start()
    thread_status.start()

running = False
def key_code(key):
    global running
    if key == pynput.keyboard.Key.esc:
        event_th.set()
        print('=============== Bot FINALIZADO ===============')
        return False
    if hasattr(key, 'char') and key.char == 'i':
        if not running:
            event_th.clear()
            start_bot()
            running = True
            print('Bot INICIADO !!!')
        else:
            event_th.set()
            running = False
            print('Bot PAUSADO !!!')

global event_th
event_th = Event()

print('===================== Tibia ToolKit =================')
print('==    Digite a tecla [i] para iniciar/pausar       ==')
print('==    Digite a tecla [esc] para finalizar o bot    ==')
print('=====================================================')

with pynput.keyboard.Listener(on_press=key_code) as listener:
    listener.join()
