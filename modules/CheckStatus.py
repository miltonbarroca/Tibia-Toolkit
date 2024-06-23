from PIL import ImageGrab, Image
import keyboard
import pyautogui as pg

LIFE_REGION = (1766, 304, 92, 5)
LIFE_COLOR = (218, 79, 79)
MANA_REGION = (1766, 316, 92, 5)
MANA_COLOR = (67, 64, 191)
WIDTH = 92

def calculate_width(percent):
    return int(WIDTH * percent / 100)

def pixel_matches_color(region, percent, color):
    result_width = calculate_width(percent)
    x = region[0] + result_width
    y = region[1] + region[3] - 1
    
    # Captura a tela apenas da região que nos interessa
    screenshot = ImageGrab.grab(bbox=(region[0], region[1], region[0] + region[2], region[1] + region[3]))
    
    # Obtém a cor do pixel na posição desejada
    pixel_color = screenshot.getpixel((result_width, region[3] - 1))
    
    # Verifica se a cor do pixel corresponde à cor desejada
    return pixel_color == color

# while True:
#     keyboard.wait('h')
#     print(pixel_matches_color(MANA_REGION, 50, MANA_COLOR))

def manager_suplies(event):
    while not event.is_set():
        if not pixel_matches_color(LIFE_REGION, 70, LIFE_COLOR):
            pg.press('2')
        if event.is_set():
            return
        else:
            if not pixel_matches_color(LIFE_REGION, 40, LIFE_COLOR):
                pg.press('1')
            if not pixel_matches_color(MANA_REGION, 80, MANA_COLOR):
                pg.press('3')
            if event.is_set():
                return
            
