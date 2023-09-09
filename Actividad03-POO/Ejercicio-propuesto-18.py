""" Ejercicio propuesto No 18,
 Realizado por Mariana Arias Montoya """

# Importamos la librería tkinter para realizar la interfaz grafica

import tkinter as tk
from tkinter import ttk

class salario(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.etiqueta_codigoEmpl = ttk.Label(parent, text="Ingrese el código del empleado:")
        self.etiqueta_codigoEmpl.place(x=20, y=20)
        self.caja_codigoEmpl = ttk.Entry(parent)
        self.caja_codigoEmpl.place(x=280, y=20, width=100)

        self.etiqueta_name = ttk.Label(parent, text="Ingrese el nombre del empleado:")
        self.etiqueta_name.place(x=20, y=50)
        self.caja_name = ttk.Entry(parent)
        self.caja_name.place(x=280, y=50, width=100)

        self.etiqueta_horasTrab = ttk.Label(parent, text="Ingrese el total de horas trabajadas al mes:")
        self.etiqueta_horasTrab.place(x=20, y=80)
        self.caja_horasTrab = ttk.Entry(parent)
        self.caja_horasTrab.place(x=280, y=80, width=100)

        self.etiqueta_valorHora = ttk.Label(parent, text="Ingrese el valor de la hora de trabajo:")
        self.etiqueta_valorHora.place(x=20, y=110)
        self.caja_valorHora = ttk.Entry(parent)
        self.caja_valorHora.place(x=280, y=110, width=100)

        self.etiqueta_porRetencion = ttk.Label(parent, text="Ingrese el porcentaje de retención en la fuente:")
        self.etiqueta_porRetencion.place(x=20, y=140)
        self.caja_porRetencion = ttk.Entry(parent)
        self.caja_porRetencion.place(x=280, y=140, width=100)

        self.boton_calcular = ttk.Button(parent, text="Calcular salario", command=self.calcularSalario)
        self.boton_calcular.place(x=150, y=180, width=100)

        self.etiqueta_resultado = ttk.Label(parent)
        self.etiqueta_resultado.place(x=20, y=220)

    def calcularSalario(self):
        codigoEmpl = int(self.caja_codigoEmpl.get())
        name = self.caja_name.get()
        horasTrab = int(self.caja_horasTrab.get())
        valorHora = int(self.caja_valorHora.get())
        porRetencion = float(self.caja_porRetencion.get())

        salarioB = horasTrab * valorHora
        retencion = int(salarioB * porRetencion)
        salarioN = salarioB - retencion

        self.etiqueta_resultado.config(text= f'{codigoEmpl} - {name} - ${salarioB} - ${salarioN}')

root = tk.Tk()
root.title("Ejercicio propuesto No 18")
root.config(width=400, height=260)
app = salario(root)
root.mainloop()