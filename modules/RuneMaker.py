from tkinter.ttk import Label , Button
from ttkthemes import ThemedTk

root = ThemedTk(theme="black", themebg=True)
root.title("MyInterface")
root.geometry("500x500+250+250")
root.resizable(False,False)

def generate_widget(widget,row,column,sticky="NSEW"):
    my_widget = widget()
    my_widget.grid(row=row,column=column,padx=5,pady=4,sticky=sticky)

lbl_food = Label(text="Hotkey Eat Food", font=("Roboto",12))
lbl_food.grid(row=0,column=0,padx=10, pady=10,sticky="W")

lbl_cast = Label(text="Hotkey Spell", font=("Roboto",12))
lbl_cast.grid(row=1,column=0,padx=10, pady=10,sticky="W")

btn_mana_position = Button(text="Mana Position")
btn_mana_position.grid(row=2,column=0, sticky="NSEW")


root.mainloop()