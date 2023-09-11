""" Ejercicio propuesto No 19,
 Realizado por Mariana Arias Montoya """

import tkinter as tk
from tkinter import ttk
import math

class TrianguloE:
    def __init__(self, root):

        self.etiqueta_lado = tk.Label(root, text="Ingrese el lado del triángulo:")
        self.etiqueta_lado.place(x=20, y=20)

        self.caja_lado = ttk.Entry(root)
        self.caja_lado.place(x=200, y=20, width=100)

        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=110, y=60, width=100)

        self.etiqueta_resultado = ttk.Label(root)
        self.etiqueta_resultado.place(x=20, y=100)


    def calcular(self):
        lado = int(self.caja_lado.get())
        perimetro = 3 * lado
        altura = round((math.sqrt(3) / 2) * lado, 3)
        area = round((math.sqrt(3) / 4) * lado**2, 3)

        self.etiqueta_resultado.config(text=f"Perímetro: {perimetro}\nAltura: {altura}\nÁrea: {area}")

root = tk.Tk()
root.title("Ejercicio propuesto No 19")
root.config(width=320, height=160)
app = TrianguloE(root)
root.mainloop()