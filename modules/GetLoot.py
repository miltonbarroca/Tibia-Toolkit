import time
import keyboard
import pyautogui as pg

loot_coordinates = [
    (2845, 451),
    (2914, 450),
    (2914, 450),
    (2911, 516),
    (2911, 589),
    (2842, 589),
    (2774, 589),
    (2774, 441)
]

def get_loot():
    keyboard.press('shift')
    for coord in loot_coordinates:
        pg.click(x=coord[0], y=coord[1], button='right')
    keyboard.release('shift')
