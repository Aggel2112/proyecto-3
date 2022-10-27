
from secrets import choice
import tkinter as tk
import random

colors = ["red", "green", "yellow", "black"]
colores = ["rojo", "verde", "amarillo", "negro"]
def cambio():
    random_colores = random.choice(colors)
    ventana.config(background=random_colores)
def nombre():
    w = tk.Label(text=random.choice(colores), font=("arial", 18), fg="black", width="10", height="1")
    w.place(x=130, y=30)

ventana = tk.Tk()
ventana.geometry ("400x300")
ventana.resizable(0,0)
ventana.title("colores")

titulo = tk.Label(text="colores", font=("arial", 18), fg="black", width="10", height="1")
titulo.place(x=130, y=30) 

btn_color = tk.Button(ventana, text="colores", command= lambda:[cambio(), nombre()])
btn_color.place(x=175, y=140)

ventana.mainloop()