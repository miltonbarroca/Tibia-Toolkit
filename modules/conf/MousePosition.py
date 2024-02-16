import pyautogui
import keyboard

def on_insert_pressed(e):
    if e.name == 'insert':
        x, y = pyautogui.position()
        print(f"Coordenadas do mouse: ({x}, {y})")

print("Pressione Insert para obter as coordenadas do mouse...")

# Adiciona o manipulador de eventos para a tecla Insert
keyboard.hook(on_insert_pressed)

# Mantém o programa em execução
keyboard.wait('esc')  # Aguarda até que a tecla Escape seja pressionada
