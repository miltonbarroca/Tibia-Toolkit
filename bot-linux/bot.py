import pyautogui as pg
import time
import actions
import json
import random
from conf import Constants

while True:
    with open(f'scripts/{Constants.SCRIPT_NAME}.json', 'r') as file:
        data = json.loads(file.read())
        for item in data:
            if not actions.check_ring():
                pg.press('f11')
            actions.next_box(item['path'], item['wait'])
            #pg.press('f3')
            #time.sleep(1)
            pg.press('f8')
            time.sleep(1)
            pg.press('f9')
            time.sleep(1)
            pg.press('f10')
            time.sleep(1)
            if not actions.check_ring():
                pg.press('f11')
            while actions.check_battle():
                pg.press('=')
                time.sleep(5)
                pg.press('l')
                #pg.press('f3')
                if not actions.check_ring():
                    pg.press('f11')
            if actions.check_player_position():
                if not actions.check_ring():
                    pg.press('f11')
                actions.next_box(item['path'], item['wait'])
                #pg.press('f3')
                #time.sleep(1)
                pg.press('f8')
                time.sleep(1)
                pg.press('f9')
                time.sleep(1)
                pg.press('f10')
                time.sleep(1)
                if not actions.check_ring():
                    pg.press('f11')
                while actions.check_battle():
                    pg.press('=')
                    time.sleep(5)
                    pg.press('l')
                    #pg.press('f3')
                    if not actions.check_ring():
                        pg.press('f11')
