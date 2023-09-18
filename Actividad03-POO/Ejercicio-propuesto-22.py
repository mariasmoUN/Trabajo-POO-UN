""" Ejercicio propuesto No 22,
 Realizado por Mariana Arias Montoya """

import tkinter as tk
from tkinter import ttk

class salario:
    def __init__(self, root):
        self.etiqueta_name = ttk.Label(root, text='Ingrese el nombre del trabajador:')
        self.etiqueta_name.place(x=20, y=20)
        self.caja_name = tk.Entry(root)
        self.caja_name.place(x=260,y=20, width=100)

        self.etiqueta_salarioHora = ttk.Label(root, text='Ingrese el salario basico por hora:')
        self.etiqueta_salarioHora.place(x=20, y=50)
        self.caja_salarioHora = tk.Entry(root)
        self.caja_salarioHora.place(x=260,y=50, width=100)

        self.etiqueta_horasT = ttk.Label(root, text='Ingrese el total de horas trabajadas al mes:')
        self.etiqueta_horasT.place(x=20, y=80)
        self.caja_horasT = ttk.Entry(root)
        self.caja_horasT.place(x=260,y=80, width=100)

        self.boton_calcular = ttk.Button(root, text="Calcular Salario", command=self.calcularSal)
        self.boton_calcular.place(x=130, y=120, width=130)

        self.etiqueta_resultado = ttk.Label(root)
        self.etiqueta_resultado.place(x=20, y=160)

    def calcularSal(self):
        name = self.caja_name.get()
        salarioH = int(self.caja_salarioHora.get())
        horasT = int(self.caja_horasT.get())

        salarioM = salarioH * horasT

        if salarioM > 450000:
            self.etiqueta_resultado.config(text=f'{name} - {salarioM}')
        else:
            self.etiqueta_resultado.config(text=f'{name}')

root = tk.Tk()
root.title("Ejercicio Propuesto No 22")
root.config(width=380, height=200)
app = salario(root)
root.mainloop()