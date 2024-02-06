import threading
import pyautogui as pg
import time
import keyboard
import random

# ATK SPELLS
# 0 - exori mas
# 9 - exori
# 8 - exori gran
# 6 - exori amp kor
# SUP SPELLS
# 7 - exeta res
# 4 - utito tempo
# i - utamo tempo

# Constantes
PAUSA_VERIFICACAO = 0.5
ATK_SPELLS = ['0', '9', '8', '6']  # HOTKEYS das magias de ataque
EXETA = ['7']  # HOTKEYS das magias de suporte
UTITO = ['4']  # HOTKEYS das magias de suporte
ATK_COOLDOWNS = [random.uniform(2, 2.4) for _ in ATK_SPELLS]

pause_programa = False
finalizar_programa = False

def combo_exeta():
    global pause_programa
    for tecla in EXETA:
        if pause_programa:
            break
        pg.press(tecla)

def combo_utito():
    global pause_programa
    for tecla in UTITO:
        if pause_programa:
            break
        pg.press(tecla)

def combo_atk():
    global pause_programa
    while not finalizar_programa:
        if pause_programa:
            time.sleep(PAUSA_VERIFICACAO)
            continue
        # Executar as sup spells no início do combo_atk
        combo_exeta()
        # hotkeys de ataque com cooldowns aleatórios:
        for tecla, cooldown in zip(ATK_SPELLS, ATK_COOLDOWNS):
            if pause_programa:
                break  # Sair do loop se pausa for acionada durante a iteração
            if tecla == '8':
                # Executar exeta antes de pressionar '8'
                combo_exeta()
            if tecla == '9':
                # Executar utito antes de pressionar '9'
                combo_utito()
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
thread_combo_atk = threading.Thread(target=combo_atk)
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
