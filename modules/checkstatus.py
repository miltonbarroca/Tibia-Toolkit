from PIL import ImageGrab, Image
import keyboard
import pyautogui as pg
import time

LIFE_REGION = (1766, 304, 92, 5)
LIFE_COLOR = (218, 79, 79)
MANA_REGION = (1766, 316, 92, 5)
MANA_COLOR = (67, 64, 191)
WIDTH = 92

EXURA_ICO_COOLDOWN = 2    # Tempo em segundos
POT_VIDA_COOLDOWN = 3    # Tempo em segundos
POT_MANA_COOLDOWN = 1.5    # Tempo em segundos

def calculate_width(percent):
    return int(WIDTH * percent / 100)

def colors_match(color1, color2, tolerance=30):
    """Verifica se duas cores são semelhantes dentro de uma tolerância."""
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def pixel_matches_color(region, percent, color, tolerance=30):
    """Verifica se o pixel na posição calculada corresponde à cor esperada dentro de uma tolerância."""
    result_width = calculate_width(percent)
    screenshot = ImageGrab.grab(bbox=(region[0], region[1], region[0] + region[2], region[1] + region[3]))
    pixel_color = screenshot.getpixel((result_width, region[3] - 1))
    return colors_match(pixel_color, color, tolerance)

def manager_suplies(event):
    last_exura_time = 0
    last_pot_vida_time = 0
    last_pot_mana_time = 0

    while not event.is_set():
        current_time = time.time()

        if current_time - last_exura_time > EXURA_ICO_COOLDOWN:
            if not pixel_matches_color(LIFE_REGION, 70, LIFE_COLOR):  # exura ico
                pg.press('2')
                last_exura_time = current_time

        if current_time - last_pot_vida_time > POT_VIDA_COOLDOWN:
            if not pixel_matches_color(LIFE_REGION, 50, LIFE_COLOR):  # pot de vida
                pg.press('1')
                last_pot_vida_time = current_time

        if current_time - last_pot_mana_time > POT_MANA_COOLDOWN:
            if not pixel_matches_color(MANA_REGION, 80, MANA_COLOR):  # pot de mana
                pg.press('3')
                last_pot_mana_time = current_time

        time.sleep(0.1)
