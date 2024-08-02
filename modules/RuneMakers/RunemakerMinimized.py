import ctypes
import time
import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import pygetwindow as gw
import threading

# Constantes
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
F1 = 0x70
F2 = 0x71
F3 = 0x72
F4 = 0x73
F5 = 0x74
F6 = 0x75
F7 = 0x76
F8 = 0x77
F9 = 0x78
F10 = 0x79
F11 = 0x7A
F12 = 0x7B

# Variáveis globais
hdwn = None
running = False
thread = None

# Função para detectar o nome da janela do Tibia
def hidden_client():
    global hdwn
    windows = pyautogui.getAllWindows()
    WINDOW_TITLE = None
    for window in windows:
        try:
            window_name = window.title.split('Tibia -')[1]
            if window_name:
                WINDOW_TITLE = window.title
        except:
            continue

    if not WINDOW_TITLE:
        messagebox.showerror("Hidden Client Tibia", "Janela do Tibia não localizada")
        raise ValueError("Janela do Tibia não localizada")

    try:
        target_window = [item for item in gw.getWindowsWithTitle(WINDOW_TITLE) if item.title == WINDOW_TITLE][0]
    except:
        messagebox.showerror("Hidden Client Tibia", "Janela do Tibia não localizada")
        raise ValueError("Janela do Tibia não localizada")

    hdwn = target_window._hWnd

# Função para enviar a mensagem de teclado
def send_message_keyboard(hdwd, key_code):
    ctypes.windll.user32.SendMessageW(hdwn, WM_KEYDOWN, key_code, 0)
    time.sleep(0.2)
    ctypes.windll.user32.SendMessageW(hdwn, WM_KEYUP, key_code, 0)

# Função principal
def main_loop(ring_key, soft_key, rune_key, food_key):
    global running
    while running:
        send_message_keyboard(hdwn, ring_key)
        time.sleep(2)
        send_message_keyboard(hdwn, soft_key)
        time.sleep(2)
        send_message_keyboard(hdwn, rune_key)
        time.sleep(2)
        send_message_keyboard(hdwn, food_key)
        time.sleep(2)

# Função para iniciar o programa
def start_program():
    global running, thread
    if not running:
        try:
            hidden_client()
        except ValueError:
            return
        ring_key = key_mapping[ring_var.get()]
        soft_key = key_mapping[soft_var.get()]
        rune_key = key_mapping[rune_var.get()]
        food_key = key_mapping[food_var.get()]
        running = True
        thread = threading.Thread(target=main_loop, args=(ring_key, soft_key, rune_key, food_key))
        thread.start()

# Função para pausar o programa
def pause_program():
    global running
    running = False
    if thread:
        thread.join()

# Mapeamento de teclas
key_mapping = {
    "F1": F1, "F2": F2, "F3": F3, "F4": F4, "F5": F5, "F6": F6, 
    "F7": F7, "F8": F8, "F9": F9, "F10": F10, "F11": F11, "F12": F12
}

# Interface gráfica
root = tk.Tk()
root.title("Tibia Automation")
root.geometry("300x250")  # Aumentando a geometria para acomodar o novo botão

style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12))
style.configure('TOptionMenu', font=('Helvetica', 12))
style.configure('TFrame', background='#f0f0f0')

main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ring_var = tk.StringVar(value="F12")
soft_var = tk.StringVar(value="F11")
rune_var = tk.StringVar(value="F10")
food_var = tk.StringVar(value="F9")

ttk.Label(main_frame, text="Ring Key:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
ring_menu = ttk.OptionMenu(main_frame, ring_var, ring_var.get(), *key_mapping.keys())
ring_menu.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E)

ttk.Label(main_frame, text="Soft Key:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
soft_menu = ttk.OptionMenu(main_frame, soft_var, soft_var.get(), *key_mapping.keys())
soft_menu.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E)

ttk.Label(main_frame, text="Rune Key:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
rune_menu = ttk.OptionMenu(main_frame, rune_var, rune_var.get(), *key_mapping.keys())
rune_menu.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

ttk.Label(main_frame, text="Food Key:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
food_menu = ttk.OptionMenu(main_frame, food_var, food_var.get(), *key_mapping.keys())
food_menu.grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)

start_button = ttk.Button(main_frame, text="Start", command=start_program)
start_button.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

pause_button = ttk.Button(main_frame, text="Pause", command=pause_program)
pause_button.grid(row=4, column=1, padx=10, pady=10, sticky=tk.E)

root.mainloop()
