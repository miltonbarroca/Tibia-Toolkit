import threading
import pyautogui as pg
import time
import keyboard
from conf import Constants

# ATK SPELLS
# 0 - exori mas
# 9 - exori
# 8 - exori gran
# 6 - exori amp kor
# SUP SPELLS
# 7 - exeta res
# 4 - utito tempo
# i - utamo tempo

pause_programa = False
finalizar_programa = False

def exeta():
    global pause_programa
    for tecla in Constants.EXETA:
        if pause_programa:
            break
        pg.press(tecla)

def utito():
    global pause_programa
    for tecla in Constants.UTITO:
        if pause_programa:
            break
        pg.press(tecla)

def auto_combo():
    global pause_programa
    while not finalizar_programa:
        if pause_programa:
            time.sleep(Constants.PAUSA_VERIFICACAO)
            continue
        exeta()
        for tecla, cooldown in zip(Constants.ATK_SPELLS, Constants.ATK_COOLDOWNS):
            if pause_programa:
                break  # Sair do loop se pausa for acionada durante a iteração
            if tecla == '8':
                exeta()
            if tecla == '9':
                utito()
            pg.press(tecla)
            time.sleep(cooldown)

def pause():
    global pause_programa, finalizar_programa
    while not finalizar_programa:
        if keyboard.is_pressed('p'):
            pause_programa = not pause_programa
            if pause_programa:
                print('pausado')
            else:
                print('retomado')
            time.sleep(1)

# Esperar pela tecla '=' antes de começar
print('Aguardando pela tecla "=" para iniciar...')
while True:
    if keyboard.is_pressed('='):
        break

# Iniciar threads após a tecla '=' ser pressionada
thread_combo_atk = threading.Thread(target=auto_combo)
thread_pause = threading.Thread(target=pause)

thread_combo_atk.start()
thread_pause.start()

# Aguardar até que o usuário pressione 'o' para finalizar o programa
while True:
    if keyboard.is_pressed('o'):
        finalizar_programa = True
        break

# Aguardar até que as threads terminem
thread_combo_atk.join()
thread_pause.join()

print('Programa finalizado')
