import pyautogui
import time
import keyboard

def get_corner_coordinates():
    print("Pressione Insert no canto superior esquerdo do quadrado e aguarde.")
    keyboard.wait("insert")

    x_region_start, y_region_start = pyautogui.position()
    print(f"Canto superior esquerdo: x={x_region_start}, y={y_region_start}")

    print("Pressione Insert no canto inferior direito do quadrado e aguarde.")
    keyboard.wait("insert")

    x_region_end, y_region_end = pyautogui.position()
    print(f"Canto inferior direito: x={x_region_end}, y={y_region_end}")

    # Calcula as dimensões da região
    region_width = x_region_end - x_region_start
    region_height = y_region_end - y_region_start
    print(f"Dimensões da região: largura={region_width}, altura={region_height}")

    return x_region_start, y_region_start, region_width, region_height

# Chamada da função para obter as coordenadas da região
x_region_start, y_region_start, region_width, region_height = get_corner_coordinates()