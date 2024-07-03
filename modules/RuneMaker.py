from tkinter.ttk import Label, Button, Combobox, Style
from tkinter import messagebox
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import os
import keyboard
import pyautogui
from conf.window import hidden_client
import json
import threading
import pynput
import time
import random


HOTKEYS = ['off', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']

root = ThemedTk(theme="black", themebg=True)
root.title("RuneMaker Pro")
#root.geometry("500x500+300+300")
root.resizable(False, False)
style = Style()
style.configure('TButton', font=("Roboto", 12))
style.configure('Ativado.TButton', foreground="green")
style.configure('Desativado.TButton', foreground="red")

def generate_widget(widget, row, column, sticky="NSEW", columnspan=None, **kwargs):
    my_widget = widget(**kwargs)
    my_widget.grid(row=row, column=column, padx=5, pady=5, columnspan=columnspan, sticky=sticky)
    return my_widget

def load_trash():
    caminho_imagem = os.path.join('img/UI/trash.png')    
    load_img = Image.open(caminho_imagem)
    resized_image = load_img.resize((20, 20))
    diretorio_principal = os.path.dirname(os.path.abspath(load_img.filename))  
    global photo_img
    photo_img = ImageTk.PhotoImage(resized_image)
    return diretorio_principal, photo_img

lbl_soft_boots = generate_widget(Label, row=0, column=0, sticky="W", text="Hotkey Soft Boots", font=("Roboto", 12))
cbx_soft_boots = generate_widget(Combobox, row=0, column=1, values=HOTKEYS, state="readonly", font=("Roboto", 12), width=12)
cbx_soft_boots.current(0)

lbl_ring = generate_widget(Label, row=1, column=0, sticky="W", text="Hotkey Ring", font=("Roboto", 12))
cbx_ring = generate_widget(Combobox, row=1, column=1, values=HOTKEYS, state="readonly", font=("Roboto", 12), width=12)
cbx_ring.current(0)

lbl_food = generate_widget(Label, row=2, column=0, sticky="W", text="Hotkey Eat Food", font=("Roboto", 12))
cbx_food = generate_widget(Combobox, row=2, column=1, values=HOTKEYS, state="readonly", font=("Roboto", 12), width=12)
cbx_food.current(0)

lbl_cast = generate_widget(Label, row=3, column=0, sticky="W", text="Hotkey Cast Spell", font=("Roboto", 12))
cbx_cast = generate_widget(Combobox, row=3, column=1, values=HOTKEYS, state="readonly", font=("Roboto", 12), width=12)
cbx_cast.current(0)
rgb = ''
mana_position = ''

def get_mana_position():
    global rgb
    global mana_position
    messagebox.showinfo(title="Mana Position", message="Posicione o mouse em cima da barra de mana e pressione a tecla insert(INS)")
    keyboard.wait('insert')
    x, y = pyautogui.position()
    rgb = pyautogui.screenshot().getpixel((x, y))
    messagebox.showinfo(title='Mana Result', message=f"X: {x} Y: {y} - RGB: {rgb}")
    lbl_mana_position.configure(text=f"({x},{y})")
    mana_position = [x,y]

btn_mana_position = generate_widget(Button, row=4, column=0, text="Mana Position",command=get_mana_position)
lbl_mana_position = generate_widget(Label, row=4, column=1, text="Empty", font=("Roboto", 12), sticky="W")

trash_dir, trash_img = load_trash()  

def clear():
    lbl_mana_position.configure(text="Empty")

btn_mana_position_trash = generate_widget(Button, row=4, column=1, image=photo_img, sticky="E",command=clear)


def opacity():
    result = hidden_client()
    if result == 1:
        btn_opacity.configure(style='Ativado.TButton')
        return
    btn_opacity.configure(style='Desativado.TButton')

btn_opacity = generate_widget(Button, row=5, column=0, text="Apply Opacity", columnspan=2, command=opacity)

def save():
    print('Salvando Configurações')
    my_data = {
        "food": {
            "value": cbx_food.get(),
            "position": cbx_food.current()
        },
        "spell": {
            "value": cbx_cast.get(),
            "position": cbx_cast.current()
        },
        "soft_boots": {
            "value": cbx_soft_boots.get(),
            "position": cbx_soft_boots.current()
        },
        "ring": {
            "value": cbx_ring.get(),
            "position": cbx_ring.current()
        },
        "mana_pos": {
            "position": mana_position,
            "rgb": rgb
        }
    }

    with open('modules/conf/infos.json', 'w') as file:
        file.write(json.dumps(my_data))


def load():
    with open('modules/conf/infos.json', 'r') as file:
        data = json.loads(file.read())
    cbx_food.current(data['food']['position'])
    cbx_cast.current(data['spell']['position'])
    cbx_ring.current(data['ring']['position'])
    cbx_soft_boots.current(data['soft_boots']['position'])
    lbl_mana_position.configure(text=data['mana_pos']['position'])
    return data

btn_load = generate_widget(Button,row=6,column=0,text="Load",command=load)

def run():
    wait_to_eat_food = 40
    time_food = time.time()

    while not myEvent.is_set():
        if data['mana_pos']['position'] is not None:
            x = data['mana_pos']['position'][0]
            y = data['mana_pos']['position'][1]

            if pyautogui.pixelMatchesColor(x, y, tuple(data['mana_pos']['rgb'])):
                if data['spell']['value'] != 'off':
                    delay = random.uniform(0.5, 1.5)
                    time.sleep(delay)
                    pyautogui.press(data['spell']['value'])

                if data['food']['value'] != 'off':
                    if int(time.time() - time_food) >= wait_to_eat_food:
                        print('comendo food')
                        pyautogui.press(data['food']['value'])
                        time_food = time.time()

                if data['soft_boots']['value'] != 'off':
                    delay = random.uniform(0.5, 2)
                    time.sleep(delay)
                    print('Equipando soft')
                    pyautogui.press(data['soft_boots']['value'])


                if data['ring']['value'] != 'off':
                    delay = random.uniform(1.5, 2.5)
                    print('Equipando ring')
                    time.sleep(delay)
                    pyautogui.press(data['ring']['value'])
    print('RuneMaker Stop')


def key_code(key):
    if key == pynput.keyboard.Key.esc:
        root.deiconify()
        myEvent.set()
        return False


def listener_keyboard():
    with pynput.keyboard.Listener(on_press=key_code) as listener:
        listener.join()

def start():
    root.iconify()
    save()
    global data
    data = load()
    global myEvent
    myEvent = threading.Event()
    global start_th
    start_th = threading.Thread(target=run)
    start_th.start()
    keyboard_th = threading.Thread(target=listener_keyboard)
    keyboard_th.start()

        
btn_start = generate_widget(Button,row=6,column=1,text="Start",command=start)



root.mainloop()
