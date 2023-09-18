""" Ejercicio propuesto No 22,
 Realizado por Mariana Arias Montoya """

import math
import tkinter as tk
from tkinter import ttk

class soluciones:
    def __init__(self, root):
        self.etiqueta_a = ttk.Label(root, text='Ingrese el valor de A:')
        self.etiqueta_a.place(x=20, y=20)
        self.caja_a = tk.Entry(root)
        self.caja_a.place(x=260,y=20, width=100)

        self.etiqueta_b = ttk.Label(root, text='Ingrese el valor de B:')
        self.etiqueta_b.place(x=20, y=50)
        self.caja_b = tk.Entry(root)
        self.caja_b.place(x=260,y=50, width=100)

        self.etiqueta_c= ttk.Label(root, text='Ingrese el valor de C:')
        self.etiqueta_c.place(x=20, y=80)
        self.caja_c = ttk.Entry(root)
        self.caja_c.place(x=260,y=80, width=100)

        self.boton_calcular = ttk.Button(root, text="Calcular", command=self.calcularSoluciones)
        self.boton_calcular.place(x=130, y=120, width=130)

        self.etiqueta_resultado = ttk.Label(root)
        self.etiqueta_resultado.place(x=20, y=160)

    def calcularSoluciones(self):
        A = float(self.caja_a.get())
        B = float(self.caja_b.get())
        C = float(self.caja_c.get())

        D = B**2 - 4*A*C

        if D > 0:
            x1 = (-B + math.sqrt(D)) / (2*A)
            x2 = (-B - math.sqrt(D)) / (2*A)
            self.etiqueta_resultado.config(text=f'Las soluciones son: x1 = {x1}, x2 = {x2}')
        else:
            x = -B / (2*A)
            self.etiqueta_resultado.config(text=f'La solución doble es: x = {x}')

root = tk.Tk()
root.title("Ejercicio Propuesto No 22")
root.config(width=380, height=200)
app = soluciones(root)
root.mainloop()