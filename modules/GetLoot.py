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
    for coord in loot_coordinates:
        # Move o mouse para a coordenada ajustada à janela
        pg.moveTo(window_left + coord[0], window_top + coord[1])
        
        # Espera um breve momento (opcional)
        time.sleep(0.1)
        
        # Clique com o botão direito
        pg.click(button='right')
        
        # Espera um breve momento antes de passar para a próxima coordenada (opcional)
        time.sleep(0.1)

# Substitua 'Nome_da_Janela' pelo título da sua janela específica
get_loot('Tibia - Brunao Qqmuda') 
