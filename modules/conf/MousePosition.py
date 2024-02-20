import pyautogui
import keyboard

def on_insert_pressed(e):
    if e.name == 'insert':
        x, y = pyautogui.position()
        rgb = pyautogui.pixel(x, y)
        print(f"Coordenadas do mouse: ({x}, {y}), RGB: {rgb}")

print("Pressione Insert para obter as coordenadas e a cor RGB do mouse...")

keyboard.hook(on_insert_pressed)
keyboard.wait('esc')