import pyautogui as pg
import time
import actions
import json
import random
from conf import Constants

contador = 0
while True:
    with open(f'scripts/{Constants.SCRIPT_NAME}.json', 'r') as file:
        data = json.loads(file.read())
        for item in data:
            if not actions.check_ring():
                pg.press('f11')
            actions.next_box(item['path'], item['wait'])
            if not actions.check_ring():
                pg.press('f11')
            while actions.check_battle():
                pg.press('=')
                time.sleep(5)
                pg.press('l')
                if not actions.check_ring():
                    pg.press('f11')
            if actions.check_player_position():
                if not actions.check_ring():
                    pg.press('f11')
                actions.next_box(item['path'], item['wait'])
                if not actions.check_ring():
                    pg.press('f11')
                while actions.check_battle():
                    pg.press('=')
                    time.sleep(5)
                    pg.press('l')
                    if not actions.check_ring():
                        pg.press('f11')
        contador = contador + 1
        if contador >= 5:
            pg.press('f3')
            contador = 0
