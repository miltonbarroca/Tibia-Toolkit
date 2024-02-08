# modules/AutoCombo.py
import threading
import pyautogui as pg
import time
import keyboard
from modules.conf import Constants

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
    global pause_programa, finalizar_programa
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

def set_finalizar_programa(value):
    global finalizar_programa
    finalizar_programa = value
