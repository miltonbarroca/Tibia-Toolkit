import threading
import pyautogui as pg
import time
import tkinter as tk
from conf import Constants

# Variáveis globais
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
                break
            if tecla == '8':
                exeta()
            if tecla == '9':
                utito()
            pg.press(tecla)
            time.sleep(cooldown)

def iniciar_combo():
    global thread_combo_atk
    thread_combo_atk = threading.Thread(target=auto_combo)
    thread_combo_atk.start()
    status_label.config(text="Combo iniciado...")

def pausar_combo():
    global pause_programa
    pause_programa = not pause_programa
    if pause_programa:
        status_label.config(text="Combo pausado")
    else:
        status_label.config(text="Combo retomado")

def finalizar_combo():
    global finalizar_programa
    finalizar_programa = True
    thread_combo_atk.join()  # Aguarda o término da thread
    status_label.config(text="Programa finalizado")

# Interface com tkinter
root = tk.Tk()
root.title("Tibia Automation Toolkit")
root.geometry("400x300")
root.configure(bg='#212121')  # Define a cor de fundo da janela

# Título
title_label = tk.Label(root, text="Tibia Automation Toolkit", font=("Helvetica", 16), fg="white", bg="#212121")
title_label.pack(pady=10)

# Botão para iniciar o combo
iniciar_button = tk.Button(root, text="Iniciar Combo", command=iniciar_combo, width=20, height=2, bg="#424242", fg="white", activebackground="#616161", activeforeground="white")
iniciar_button.pack(pady=5)

# Botão para pausar/retomar o combo
pausar_button = tk.Button(root, text="Pausar/Retomar Combo", command=pausar_combo, width=20, height=2, bg="#424242", fg="white", activebackground="#616161", activeforeground="white")
pausar_button.pack(pady=5)

# Botão para finalizar o combo
finalizar_button = tk.Button(root, text="Finalizar Programa", command=finalizar_combo, width=20, height=2, bg="#424242", fg="white", activebackground="#616161", activeforeground="white")
finalizar_button.pack(pady=5)

# Label para status
status_label = tk.Label(root, text="Aguardando...", font=("Helvetica", 12), fg="white", bg="#212121")
status_label.pack(pady=20)

# Inicia a interface
root.mainloop()
