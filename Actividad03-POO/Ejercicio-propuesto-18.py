""" Ejercicio propuesto No 18,
 Realizado por Mariana Arias Montoya """

# Importamos la librería tkinter para realizar la interfaz grafica
import tkinter as tk
from tkinter import ttk

def calcularSalario():
    codigoEmpl = int(caja_codigoEmpl.get())
    name = caja_name.get()
    horasTrab = int(caja_horasTrab.get())
    valorHora = int(caja_valorHora.get())
    porRetencion = float(caja_porRetencion.get())

    salarioB = horasTrab * valorHora
    retencion = int(salarioB * porRetencion)
    salarioN = salarioB - retencion

    etiqueta_resultado.config(text= f'{codigoEmpl} - {name} - ${salarioB} - ${salarioN}')

root = tk.Tk()
root.title("Ejercicio propuesto No 18")
root.config(width=400, height=260)

etiqueta_codigoEmpl = ttk.Label(text="Ingrese el código del empleado:")
etiqueta_codigoEmpl.place(x=20, y=20)
caja_codigoEmpl = ttk.Entry()
caja_codigoEmpl.place(x=280, y=20, width=100)

etiqueta_name = ttk.Label(text="Ingrese el nombre del empleado:")
etiqueta_name.place(x=20, y=50)
caja_name = ttk.Entry()
caja_name.place(x=280, y=50, width=100)

etiqueta_horasTrab = ttk.Label(text="Ingrese el total de horas trabajadas al mes:")
etiqueta_horasTrab.place(x=20, y=80)
caja_horasTrab = ttk.Entry()
caja_horasTrab.place(x=280, y=80, width=100)

etiqueta_valorHora = ttk.Label(text="Ingrese el valor de la hora de trabajo:")
etiqueta_valorHora.place(x=20, y=110)
caja_valorHora = ttk.Entry()
caja_valorHora.place(x=280, y=110, width=100)

etiqueta_porRetencion = ttk.Label(text="Ingrese el porcentaje de retención en la fuente:")
etiqueta_porRetencion.place(x=20, y=140)
caja_porRetencion = ttk.Entry()
caja_porRetencion.place(x=280, y=140, width=100)

boton_calcular = ttk.Button(text="Calcular salario", command=calcularSalario)
boton_calcular.place(x=150, y=180, width=100)

etiqueta_resultado = ttk.Label()
etiqueta_resultado.place(x=20, y=220)

root.mainloop()