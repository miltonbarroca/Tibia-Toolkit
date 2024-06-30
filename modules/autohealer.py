import threading
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk
from PIL import ImageGrab
import pyautogui as pg
import keyboard
from healer import getHpPercentage
import time


def manager_supplies(stop_event, pause_event, life_threshold, life_button, exura_threshold, exura_button, mana_threshold, mana_button):
        
    while not stop_event.is_set():
        if pause_event.is_set():
            stop_event.wait()
            continue

        life = getHpPercentage()

        if life <= exura_threshold:
            pg.hotkey(exura_button)
            time.sleep(0.100)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Supply Manager")
        self.root.geometry("400x520")

        style = ttk.Style()
        style.theme_use('black')

        # Apply custom styles
        style.configure('TButton', font=("Roboto", 12))
        style.configure('Ativado.TButton', foreground="green")
        style.configure('Desativado.TButton', foreground="red")

        self.life_thresholds = {
            "Vida Baixa": 30,
            "Vida Média": 60,
            "Vida Alta": 90
        }

        self.exura_thresholds = {
            "Exura Baixa": 30,
            "Exura Média": 60,
            "Exura Alta": 90
        }

        self.mana_thresholds = {
            "Mana Baixa": 30,
            "Mana Média": 60,
            "Mana Alta": 90
        }

        self.create_widgets()
        
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()
        self.thread = None

        keyboard.add_hotkey('=', self.toggle_pause_resume)
        keyboard.add_hotkey('esc', self.stop)

    def create_widgets(self):
        life_options = list(self.life_thresholds.keys())
        exura_options = list(self.exura_thresholds.keys())
        mana_options = list(self.mana_thresholds.keys())

        label_font = ('Helvetica', 12, 'bold')
        entry_font = ('Helvetica', 12)

        ttk.Label(self.root, text="Life Threshold:", font=label_font).pack(pady=(10, 0))
        self.life_threshold = tk.StringVar(self.root)
        life_menu = ttk.OptionMenu(self.root, self.life_threshold, life_options[1], *life_options)
        life_menu.pack(pady=(0, 10))
        self.life_threshold.set(life_options[1])

        ttk.Label(self.root, text="Life Button:", font=label_font).pack(pady=(10, 0))
        self.life_button = ttk.Entry(self.root, font=entry_font)
        self.life_button.pack(pady=(0, 10))
        self.life_button.bind("<KeyPress>", lambda event, widget=self.life_button: self.on_key_press(event, widget))

        ttk.Label(self.root, text="Exura Threshold:", font=label_font).pack(pady=(10, 0))
        self.exura_threshold = tk.StringVar(self.root)
        exura_menu = ttk.OptionMenu(self.root, self.exura_threshold, exura_options[1], *exura_options)
        exura_menu.pack(pady=(0, 10))
        self.exura_threshold.set(exura_options[1])

        ttk.Label(self.root, text="Exura Button:", font=label_font).pack(pady=(10, 0))
        self.exura_button = ttk.Entry(self.root, font=entry_font)
        self.exura_button.pack(pady=(0, 10))
        self.exura_button.bind("<KeyPress>", lambda event, widget=self.exura_button: self.on_key_press(event, widget))

        ttk.Label(self.root, text="Mana Threshold:", font=label_font).pack(pady=(10, 0))
        self.mana_threshold = tk.StringVar(self.root)
        mana_menu = ttk.OptionMenu(self.root, self.mana_threshold, mana_options[1], *mana_options)
        mana_menu.pack(pady=(0, 10))
        self.mana_threshold.set(mana_options[1])

        ttk.Label(self.root, text="Mana Button:", font=label_font).pack(pady=(0, 20))
        self.mana_button = ttk.Entry(self.root, font=entry_font)
        self.mana_button.pack(pady=(0, 20))
        self.mana_button.bind("<KeyPress>", lambda event, widget=self.mana_button: self.on_key_press(event, widget))

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        self.start_button = ttk.Button(button_frame, text="Start", command=self.start, width=15, style='Ativado.TButton')
        self.start_button.pack(side="left", padx=5)

        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop, width=15, style='Desativado.TButton')
        self.stop_button.pack(side="left", padx=5)
        
        signature_font = ('Helvetica', 10, 'italic')
        signature_label = ttk.Label(self.root, text="Tibia Tool Kit", font=signature_font)
        signature_label.pack(side="bottom", pady=(5, 5))

    def on_key_press(self, event, target_widget):
        target_widget.delete(0, tk.END)
        if event.keysym in ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']:
            target_widget.insert(0, event.keysym)
        
    def start(self):
        if not all([self.life_button.get(), self.exura_button.get(), self.mana_button.get()]):
            print("Error: One or more button inputs are empty.")
            return 

        if self.thread is None or not self.thread.is_alive():
            self.stop_event.clear()
            self.pause_event.clear()

            life_threshold_str = self.life_threshold.get()
            life_threshold = self.life_thresholds[life_threshold_str]
            life_button = self.life_button.get()
            
            exura_threshold_str = self.exura_threshold.get()
            exura_threshold = self.exura_thresholds[exura_threshold_str]
            exura_button = self.exura_button.get()
            
            mana_threshold_str = self.mana_threshold.get()
            mana_threshold = self.mana_thresholds[mana_threshold_str]
            mana_button = self.mana_button.get()
            
            self.thread = threading.Thread(target=manager_supplies, args=(self.stop_event, self.pause_event, life_threshold, life_button, exura_threshold, exura_button, mana_threshold, mana_button))
            self.thread.start()
            self.start_button.config(state='disabled')
            self.root.iconify()

    def pause(self):
        self.pause_event.set()

    def resume(self):
        self.pause_event.clear()

    def toggle_pause_resume(self):
        if self.pause_event.is_set():
            self.resume()
        else:
            self.pause()

    def stop(self):
        self.stop_event.set()
        self.pause_event.clear()
        if self.thread is not None:
            self.thread.join()
        self.root.quit()

if __name__ == "__main__":
    root = ThemedTk(theme="black", themebg=True)
    app = App(root)
    root.mainloop()
