"""
from .logic.Concessionarie import Concessionarie
from .model import Car, Tractor

concesionaria = Concessionarie()
Car(brand="Toyota")
Tractor(brand="John Deere")

print(concesionaria.find(Car, Tractor))
"""
from view.MainWindow import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

"""

import tkinter as tk
from tkinter import messagebox

def validar_entrada(nuevo_texto):
    if nuevo_texto == "":
        return True
    if nuevo_texto in ("."):
        return True
    try:
        float(nuevo_texto)
        return True
    except ValueError:
        messagebox.showerror("Error de entrada", "Solo se permiten números positivo(incluyendo decimales) en este campo.")
        return False
    

def accion(texto):
    global a
    a.config(text=f"{texto}")

ventana = tk.Tk()
ventana.title("Validar Entrada")
ventana.geometry("300x150")

vcmd = (ventana.register(validar_entrada), '%P')

entrada = tk.Entry(ventana, validate="key", validatecommand=vcmd)
entrada.pack()
a = tk.Label(ventana, bg="white", text="aqui")
botom = tk.Button(ventana, text="botommm", command=lambda:accion(entrada.get()))
botom.pack()
a.pack()
ventana.mainloop()
"""
