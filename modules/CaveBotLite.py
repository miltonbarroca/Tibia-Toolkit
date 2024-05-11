import pyautogui as pg
import time
import actions
import AutoEquip
from threading import Thread
import json
from conf import Constants
import CheckStatus
import keyboard

'''
USE ESSE MODULO PARA HUNTS MAIS SIMPLES COMO STONEREFINER OU ITENS DE IMBUI
'''

class CheckRingThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            AutoEquip.check_ring()
            CheckStatus.check_status('life', 1, *Constants.PIXEL_LIFE, Constants.COR_LIFE, '1')
            time.sleep(1)

def main():
    check_ring_thread = CheckRingThread()
    check_ring_thread.start()

    while True:
        with open(f'scripts/{Constants.SCRIPT_NAME}.json', 'r') as file:
            data = json.loads(file.read())
            while True:
                if actions.check_battle():
                    pg.press('space')
                    time.sleep(9)
                    actions.get_loot()
                    break  # Saia do loop interno quando a batalha for encontrada
                else:
                    for item in data:
                        actions.next_box(item['path'], item['wait'])
                        if actions.check_battle():
                            pg.press('space')
                            time.sleep(12)
                            actions.get_loot()
                            break  # Saia do loop interno quando a batalha for encontrada


if __name__ == "__main__":
    keyboard.wait('h')
    main()
