import pyautogui as pg
import time

def check_status(name, delay, x, y, rgb, button_names):
    print(f'checando {name}')
    time.sleep(2)
    
    while pg.pixelMatchesColor(x, y, rgb):
        for button_name in button_names:
            pg.press(button_name)
            time.sleep(delay)