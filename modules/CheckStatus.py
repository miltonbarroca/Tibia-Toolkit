import pyautogui as pg
import time
from conf import Constants
import keyboard

def check_status(name, delay, button_name):
    print(f'Checando {name}')
    time.sleep(2)
    
    while True:
        try:
            if pg.locateOnScreen('img/empty.png', region=Constants.BARS_REGION) is not None:
                pg.press(button_name)
                time.sleep(delay)
            else:
                print(f'{name} não encontrado, parando de verificar.')
                return True
        except pg.ImageNotFoundException:
            print(f'{name} não encontrado, parando de verificar.')
            return False

# Exemplo de uso
# keyboard.wait('h')


# if check_status('HP', 1, '1'):  # Exemplo para a barra de vida
#     print("low HP.")
# else:
#     print("HP cheio.")

# if check_status('MP', 2.2, '3'):  # Exemplo para a barra de mana
#     print("low MP")
# else:
#     print("MP cheio.")