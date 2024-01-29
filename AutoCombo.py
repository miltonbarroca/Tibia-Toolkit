import threading
import pyautogui as pg
import time
import keyboard
import random

#ATK SPELLS
#0 - exori mas
#9 - exori
#8 - exori gran
#6 - exori amp kor
#SUP SPELLS
#7 - exeta res
#4 - utito tempo
#i - utamo tempo

# Constantes
PAUSA_VERIFICACAO = 0.5
ATK_SPELLS = ['0', '9', '8', '6']  # HOTKEYS das magias de ataque
SUP_SPELLS = ['7']  # Adicione as HOTKEYS das magias de suporte aqui
ATK_INTERVALOS = [random.uniform(2, 2.5) for _ in ATK_SPELLS]

pause_programa = False
finalizar_programa = False

def combo_sup():
    global pause_programa
    for tecla in SUP_SPELLS:
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
        combo_sup()
        # hotkeys de ataque com intervalos aleatórios:
        for tecla, intervalo in zip(ATK_SPELLS, ATK_INTERVALOS):
            if pause_programa:
                break  # Sair do loop se pausa for acionada durante a iteração
            pg.press(tecla)
            time.sleep(intervalo)

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

# Iniciar threads
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