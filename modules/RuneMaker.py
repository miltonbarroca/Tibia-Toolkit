from tkinter.ttk import Label , Button, Combobox
from ttkthemes import ThemedTk

HOTKEYS = ['off','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12']

root = ThemedTk(theme="black", themebg=True)
root.title("MyInterface")
root.geometry("500x500+250+250")
root.resizable(False,False)

def generate_widget(widget,row,column,sticky="NSEW", **kwargs):
    my_widget = widget(**kwargs)
    my_widget.grid(row=row,column=column,padx=5,pady=4,sticky=sticky)
    return my_widget

lbl_food = generate_widget(Label,row=0,column=0,sticky="W",text="Hotkey Eat Food",font=("Roboto",12))
cbx_food = generate_widget(Combobox,row=0,column=1,values=HOTKEYS,state="readonly",font=("Roboto",12),width=12)
cbx_food.current(0)

lbl_cast = generate_widget(Label,row=1,column=0,sticky="W",text="Hotkey Eat Food",font=("Roboto",12))
cbx_cast = generate_widget(Combobox,row=1,column=1,values=HOTKEYS,state="readonly",font=("Roboto",12),width=12)
cbx_cast.current(0)


btn_mana_position = generate_widget(Button, row=2,column=0,text="Mana Position")





root.mainloop()