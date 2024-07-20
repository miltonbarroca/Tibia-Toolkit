import ctypes
import pygetwindow as gw
import pyautogui
import win32gui
import threading
import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
import keyboard

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
LWA_ALPHA = 0x00000002

def get_window_opacity(hwnd):
    ex_style = win32gui.GetWindowLong(hwnd, GWL_EXSTYLE)
    if ex_style & WS_EX_LAYERED:
        style = ctypes.c_ulong()
        opacity = ctypes.c_byte()
        ctypes.windll.user32.GetLayeredWindowAttributes(hwnd, None, ctypes.byref(opacity), ctypes.byref(style))
        return opacity.value
    else:
        return None

def hidden_client():
    windows = pyautogui.getAllWindows()
    for window in windows:
        try:
            window_name = window.title.split('Tibia -')[1]
            if window_name:
                WINDOW_TITLE = window.title
        except:
            continue

    try:
        target_window = [item for item in gw.getWindowsWithTitle(WINDOW_TITLE) if item.title == WINDOW_TITLE][0]
    except:
        pyautogui.alert(title="Hidden Client Tibia", text='Janela do Tibia não localizada')
        raise ValueError('Janela do Tibia não localizada')

    target_hwnd = target_window._hWnd

    OPACITY = 255
    current_opacity = get_window_opacity(target_hwnd)
    if current_opacity == -1:
        OPACITY = 1
    print('OPACITY', OPACITY)
    ex_style = ctypes.windll.user32.GetWindowLongA(target_hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongA(target_hwnd, GWL_EXSTYLE, ex_style | WS_EX_LAYERED)
    ctypes.windll.user32.SetLayeredWindowAttributes(target_hwnd, 0, OPACITY, LWA_ALPHA)
    print("Opacidade da janela modificada.")
    if current_opacity is not None:
        print(f"Opacidade atual da janela: {current_opacity}")
    else:
        print("A janela não é uma janela de camada (layered window).")
    return OPACITY

LIFE_REGION = (1766, 304, 92, 5)
LIFE_COLOR = (218, 79, 79)
MANA_REGION = (1766, 316, 92, 5)
MANA_COLOR = (67, 64, 191)
WIDTH = 92

def calculate_width(percent):
    return int(WIDTH * percent / 100)

def pixel_matches_color(region, percent, color):
    result_width = calculate_width(percent)
    x = region[0] + result_width
    y = region[1] + region[3] - 1

    screenshot = ImageGrab.grab(bbox=(region[0], region[1], region[0] + region[2], region[1] + region[3]))
    pixel_color = screenshot.getpixel((result_width, region[3] - 1))
    return pixel_color == color

def manager_suplies(event, life_key, mana_key, exura_key, life_percent, mana_percent, exura_percent):
    while not event.is_set():
        if not pixel_matches_color(LIFE_REGION, life_percent, LIFE_COLOR):
            pyautogui.press(life_key)
        if event.is_set():
            return
        if not pixel_matches_color(MANA_REGION, mana_percent, MANA_COLOR):
            pyautogui.press(mana_key)
        if event.is_set():
            return
        if not pixel_matches_color(LIFE_REGION, exura_percent, LIFE_COLOR):
            pyautogui.press(exura_key)
        if event.is_set():
            return

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("TTK Autohealer")

        self.life_key = tk.StringVar(value='2')
        self.mana_key = tk.StringVar(value='3')
        self.exura_key = tk.StringVar(value='e')
        self.life_percent = tk.StringVar(value='70')
        self.mana_percent = tk.StringVar(value='80')
        self.exura_percent = tk.StringVar(value='50')

        ttk.Label(root, text="Life Key:").grid(row=0, column=0)
        ttk.Entry(root, textvariable=self.life_key).grid(row=0, column=1)

        ttk.Label(root, text="Mana Key:").grid(row=1, column=0)
        ttk.Entry(root, textvariable=self.mana_key).grid(row=1, column=1)

        ttk.Label(root, text="Exura Key:").grid(row=2, column=0)
        ttk.Entry(root, textvariable=self.exura_key).grid(row=2, column=1)

        ttk.Label(root, text="Life Percentage:").grid(row=3, column=0)
        life_percentages = ttk.Combobox(root, textvariable=self.life_percent, values=[str(i) for i in range(10, 100, 10)])
        life_percentages.grid(row=3, column=1)

        ttk.Label(root, text="Mana Percentage:").grid(row=4, column=0)
        mana_percentages = ttk.Combobox(root, textvariable=self.mana_percent, values=[str(i) for i in range(10, 100, 10)])
        mana_percentages.grid(row=4, column=1)

        ttk.Label(root, text="Exura Percentage:").grid(row=5, column=0)
        exura_percentages = ttk.Combobox(root, textvariable=self.exura_percent, values=[str(i) for i in range(10, 100, 10)])
        exura_percentages.grid(row=5, column=1)

        self.start_button = ttk.Button(root, text="Start", command=self.start)
        self.start_button.grid(row=6, column=0)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop, state='disabled')
        self.stop_button.grid(row=6, column=1)
        
        self.apply_opacity_button = ttk.Button(root, text="Apply Opacity", command=self.apply_opacity)
        self.apply_opacity_button.grid(row=7, column=0, columnspan=2)

        self.event = threading.Event()

        self.root.iconify()

        keyboard.add_hotkey('=', self.pause_resume)
        keyboard.add_hotkey('esc', self.exit)

    def start(self):
        self.event.clear()
        self.thread = threading.Thread(target=manager_suplies, args=(
            self.event, self.life_key.get(), self.mana_key.get(), self.exura_key.get(),
            int(self.life_percent.get()), int(self.mana_percent.get()), int(self.exura_percent.get())))
        self.thread.start()
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')

    def stop(self):
        self.event.set()
        self.thread.join()
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')

    def pause_resume(self):
        if self.event.is_set():
            self.event.clear()
            self.start()
        else:
            self.stop()

    def exit(self):
        self.stop()
        self.root.destroy()

    def apply_opacity(self):
        hidden_client()

root = tk.Tk()
app = App(root)
root.mainloop()
