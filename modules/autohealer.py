import threading
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import pyautogui as pg
import keyboard
from healer import getHpPercentage, getManaPercentage
import time

def manager_supplies(stop_event, pause_event, life_threshold, life_button, exura_threshold, exura_button, mana_threshold, mana_button):
    while not stop_event.is_set():
        if pause_event.is_set():
            stop_event.wait()
            continue

        life = getHpPercentage()
        mana = getManaPercentage()

        if life is not None:
            if life <= exura_threshold:
                pg.hotkey(exura_button)
                time.sleep(0.100)

            if life <= life_threshold:
                pg.hotkey(life_button)
                time.sleep(0.100)

        if mana is not None and mana <= mana_threshold:
            pg.hotkey(mana_button)
            time.sleep(0.100)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Healer ")
        self.root.geometry("400x400")

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

        self.load_images()
        self.create_background()
        self.create_widgets()
        
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()
        self.thread = None

        keyboard.add_hotkey('=', self.toggle_pause_resume)
        keyboard.add_hotkey('esc', self.stop)

    def load_images(self):
        self.health_image = Image.open("img/UI/health.png").convert("RGBA")
        self.health_image = ImageOps.contain(self.health_image, (30, 30))
        self.health_image = ImageTk.PhotoImage(self.health_image)

        self.exura_image = Image.open("img/UI/exura.png").convert("RGBA")
        self.exura_image = ImageOps.contain(self.exura_image, (30, 30))
        self.exura_image = ImageTk.PhotoImage(self.exura_image)

        self.mana_image = Image.open("img/UI/mana.png").convert("RGBA")
        self.mana_image = ImageOps.contain(self.mana_image, (30, 30))
        self.mana_image = ImageTk.PhotoImage(self.mana_image)

        self.background_image = Image.open("img/UI/background.png").convert("RGBA")

    def create_background(self):
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack(fill="both", expand=True)

        self.update_background_image()

        self.root.bind("<Configure>", self.on_resize)

    def update_background_image(self):
        width, height = self.root.winfo_width(), self.root.winfo_height()
        resized_bg = self.background_image.resize((width, height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized_bg)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

    def on_resize(self, event):
        self.update_background_image()

    def create_widgets(self):
        life_options = list(self.life_thresholds.keys())
        exura_options = list(self.exura_thresholds.keys())
        mana_options = list(self.mana_thresholds.keys())

        label_font = ('Times New Roman', 13, 'bold')
        entry_font = ('Times New Roman', 13)

        # Health Widgets
        health_frame = ttk.Frame(self.root)
        self.canvas.create_window(200, 50, window=health_frame, anchor="center")

        ttk.Label(health_frame, text="Life Threshold:", font=label_font).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.life_threshold = tk.StringVar(self.root)
        life_menu = ttk.OptionMenu(health_frame, self.life_threshold, life_options[1], *life_options)
        life_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.life_threshold.set(life_options[1])

        ttk.Label(health_frame, image=self.health_image).grid(row=0, column=2, padx=(10, 0), pady=5)

        ttk.Label(health_frame, text="Life Button:", font=label_font).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.life_button = ttk.Entry(health_frame, font=entry_font, width=10)
        self.life_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.life_button.bind("<KeyPress>", lambda event, widget=self.life_button: self.on_key_press(event, widget))

        # Exura Widgets
        exura_frame = ttk.Frame(self.root)
        self.canvas.create_window(200, 150, window=exura_frame, anchor="center")

        ttk.Label(exura_frame, text="Exura Threshold:", font=label_font).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.exura_threshold = tk.StringVar(self.root)
        exura_menu = ttk.OptionMenu(exura_frame, self.exura_threshold, exura_options[1], *exura_options)
        exura_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.exura_threshold.set(exura_options[1])

        ttk.Label(exura_frame, image=self.exura_image).grid(row=0, column=2, padx=(10, 0), pady=5)

        ttk.Label(exura_frame, text="Exura Button:", font=label_font).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.exura_button = ttk.Entry(exura_frame, font=entry_font, width=10)
        self.exura_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.exura_button.bind("<KeyPress>", lambda event, widget=self.exura_button: self.on_key_press(event, widget))

        # Mana Widgets
        mana_frame = ttk.Frame(self.root)
        self.canvas.create_window(200, 250, window=mana_frame, anchor="center")

        ttk.Label(mana_frame, text="Mana Threshold:", font=label_font).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.mana_threshold = tk.StringVar(self.root)
        mana_menu = ttk.OptionMenu(mana_frame, self.mana_threshold, mana_options[1], *mana_options)
        mana_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.mana_threshold.set(mana_options[1])

        ttk.Label(mana_frame, image=self.mana_image).grid(row=0, column=2, padx=(10, 0), pady=5)

        ttk.Label(mana_frame, text="Mana Button:", font=label_font).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.mana_button = ttk.Entry(mana_frame, font=entry_font, width=10)
        self.mana_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.mana_button.bind("<KeyPress>", lambda event, widget=self.mana_button: self.on_key_press(event, widget))

        # Control Buttons
        button_frame = ttk.Frame(self.root)
        self.canvas.create_window(200, 350, window=button_frame, anchor="center")

        self.start_button = ttk.Button(button_frame, text="Start", command=self.start, width=15, style='Ativado.TButton')
        self.start_button.pack(side="left", padx=5)

        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop, width=15, style='Desativado.TButton')
        self.stop_button.pack(side="left", padx=5)
        
        signature_font = ('Helvetica', 10, 'italic')
        signature_label = ttk.Label(self.root, text="Tibia Tool Kit", font=signature_font)
        self.canvas.create_window(200, 380, window=signature_label, anchor="center")

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
