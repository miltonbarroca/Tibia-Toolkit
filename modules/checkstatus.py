import threading
import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
import keyboard
import pyautogui as pg

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

def manager_suplies(event, life_key, mana_key, life_percent, mana_percent):
    while not event.is_set():
        if not pixel_matches_color(LIFE_REGION, life_percent, LIFE_COLOR):
            pg.press(life_key)
        if event.is_set():
            return
        if not pixel_matches_color(MANA_REGION, mana_percent, MANA_COLOR):
            pg.press(mana_key)
        if event.is_set():
            return

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("TTK Autohealer")

        self.life_key = tk.StringVar(value='2')
        self.mana_key = tk.StringVar(value='3')
        self.life_percent = tk.StringVar(value='70')
        self.mana_percent = tk.StringVar(value='80')

        ttk.Label(root, text="Life Key:").grid(row=0, column=0)
        ttk.Entry(root, textvariable=self.life_key).grid(row=0, column=1)

        ttk.Label(root, text="Mana Key:").grid(row=1, column=0)
        ttk.Entry(root, textvariable=self.mana_key).grid(row=1, column=1)

        ttk.Label(root, text="Life Percentage:").grid(row=2, column=0)
        life_percentages = ttk.Combobox(root, textvariable=self.life_percent, values=[str(i) for i in range(10, 100, 10)])
        life_percentages.grid(row=2, column=1)

        ttk.Label(root, text="Mana Percentage:").grid(row=3, column=0)
        mana_percentages = ttk.Combobox(root, textvariable=self.mana_percent, values=[str(i) for i in range(10, 100, 10)])
        mana_percentages.grid(row=3, column=1)

        self.start_button = ttk.Button(root, text="Start", command=self.start)
        self.start_button.grid(row=4, column=0)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop, state='disabled')
        self.stop_button.grid(row=4, column=1)

        self.event = threading.Event()

        self.root.iconify()

        keyboard.add_hotkey('=', self.pause_resume)
        keyboard.add_hotkey('esc', self.exit)

    def start(self):
        self.event.clear()
        self.thread = threading.Thread(target=manager_suplies, args=(
            self.event, self.life_key.get(), self.mana_key.get(),
            int(self.life_percent.get()), int(self.mana_percent.get())))
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

root = tk.Tk()
app = App(root)
root.mainloop()
