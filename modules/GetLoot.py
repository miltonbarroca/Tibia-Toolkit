import time
import keyboard
import pyautogui as pg
import pygetwindow as gw

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

def get_window_position(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        return window.left, window.top
    except IndexError:
        raise Exception(f"Window with title '{window_title}' not found")

def get_loot(window_title):
    window_left, window_top = get_window_position(window_title)
    keyboard.wait('h')
    
    # Pressiona a tecla Shift
    keyboard.press('shift')
    
    for coord in loot_coordinates:
        pg.moveTo(window_left + coord[0], window_top + coord[1])
        pg.click(button='right')
    
    # Libera a tecla Shift após o loop
    keyboard.release('shift')

# Substitua 'Nome_da_Janela' pelo título da sua janela específica
get_loot('Tibia - Brunao Qqmuda')
