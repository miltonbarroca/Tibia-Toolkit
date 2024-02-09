from tkinter.ttk import Label
from ttkthemes import ThemedTk

root = ThemedTk(theme="black", themebg=True)
root.title("MyInterface")
root.geometry("500x500+250+250")
root.resizable(False,False)

lbl_food = Label(text="Hotkey Eat Food")
lbl_food.grid(row=0,column=0,padx=10, pady=10)

lbl_cast = Label(text="Hotkey Spell")
lbl_cast.grid(row=1,column=0)

root.mainloop()