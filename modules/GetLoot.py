import time
import keyboard
import pyautogui as pg

loot_coordinates = [
    (2849, 478),
    (2907, 479),
    (2914, 545),
    (2911, 613),
    (2843, 613),
    (2771, 607),
    (2772, 539),
    (2771, 477)
]

def get_loot():
    keyboard.press('shift')
    for coord in loot_coordinates:
        pg.click(x=coord[0], y=coord[1], button='right')
    keyboard.release('shift')

get_loot()