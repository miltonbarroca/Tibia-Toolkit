import time
import keyboard
import pyautogui as pg

loot_coordinates = [
    (923, 305),
    (991, 322),
    (992, 389),
    (1000, 461),
    (926, 454),
    (853, 442),
    (851, 383),
    (852, 328)
]

def get_loot():
    keyboard.press('shift')
    for coord in loot_coordinates:
        pg.click(x=coord[0], y=coord[1], button='right')
    keyboard.release('shift')

get_loot()
