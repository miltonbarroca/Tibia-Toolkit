import threading
import pyautogui as pg
import time
import keyboard

pause_programa = False
finalizar_programa = False

def x():
    while not finalizar_programa:
        if pause_programa:
            time.sleep(0.5)  # Aguarda um segundo antes de verificar novamente
            continue

            #hotkeys:
        pg.press('7')
        time.sleep(0.1)
        pg.press('0')
        time.sleep(2)
        pg.press('9')
        time.sleep(2)
        pg.press('8')
        time.sleep(2)
        pg.press('6')

def y():
    global pause_programa, finalizar_programa
    while not finalizar_programa:
        if keyboard.is_pressed('p'):
            pause_programa = not pause_programa
            if pause_programa:
                print('pausado')
            else:
                print('retomado')
            time.sleep(1)  # Aguarda um segundo para evitar pressionar 'p' várias vezes

# Iniciar threads
thread_x = threading.Thread(target=x)
thread_y = threading.Thread(target=y)

thread_x.start()
thread_y.start()

# Aguardar até que o usuário pressione 'o' para finalizar o programa
while True:
    if keyboard.is_pressed('o'):
        finalizar_programa = True
        break

# Aguardar até que as threads terminem
thread_x.join()
thread_y.join()

print('Programa finalizado')
