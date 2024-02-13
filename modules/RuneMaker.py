from tkinter.ttk import Label, Button, Combobox, Style
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import os

HOTKEYS = ['off', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']

root = ThemedTk(theme="black", themebg=True)
root.title("MyInterface")
#root.geometry("500x500+250+250")
root.resizable(False, False)
style = Style()
style.configure('TButton', font=("Roboto", 12))

def generate_widget(widget, row, column, sticky="NSEW", columnspan=None, **kwargs):
    my_widget = widget(**kwargs)
    my_widget.grid(row=row, column=column, padx=5, pady=5, columnspan=columnspan, sticky=sticky)
    return my_widget


def load_thrash():
    caminho_imagem = os.path.join('img', 'trash.png')    
    load_img = Image.open(caminho_imagem)
    resized_image = load_img.resize((20, 20))
    diretorio_principal = os.path.dirname(os.path.abspath(load_img.filename))  

    # Make photo_img a global variable
    global photo_img
    photo_img = ImageTk.PhotoImage(resized_image)

    return diretorio_principal, photo_img


lbl_food = generate_widget(Label, row=0, column=0, sticky="W", text="Hotkey Eat Food", font=("Roboto", 12))
cbx_food = generate_widget(Combobox, row=0, column=1, values=HOTKEYS, state="readonly", font=("Roboto", 12), width=12)
cbx_food.current(0)

lbl_cast = generate_widget(Label, row=1, column=0, sticky="W", text="Hotkey Cast Spell", font=("Roboto", 12))
cbx_cast = generate_widget(Combobox, row=1, column=1, values=HOTKEYS, state="readonly", font=("Roboto", 12), width=12)
cbx_cast.current(0)

btn_mana_position = generate_widget(Button, row=2, column=0, text="Mana Position")
lbl_mana_position = generate_widget(Label, row=2, column=1, text="Empty", font=("Roboto", 12), sticky="W")


trash_dir, trash_img = load_thrash()  
btn_mana_position_trash = generate_widget(Button, row=2, column=1, image=photo_img, sticky="E")


btn_opacity = generate_widget(Button, row=3, column=0, text="Aplly Opacity", columnspan=2)

btn_load = generate_widget(Button,row=4,column=0,text="Load")
btn_start = generate_widget(Button,row=4,column=1,text="Start")

root.mainloop()
