""" Ejercicio resuelto No 10,
 Realizado por Mariana Arias Montoya """

import tkinter as tk
from tkinter import ttk

class MatriculaU:
    def __init__(self, root):
        self.etiqueta_ni = ttk.Label(root, text='Ingrese el numero de inscripcion:')
        self.etiqueta_ni.place(x=20, y=20)
        self.caja_ni = ttk.Entry(root)
        self.caja_ni.place(x=260,y=20, width=100)

        self.etiqueta_nom = ttk.Label(root, text='Ingrese su nombre:')
        self.etiqueta_nom.place(x=20, y=50)
        self.caja_nom = ttk.Entry(root)
        self.caja_nom.place(x=260,y=50, width=100)

        self.etiqueta_pat = ttk.Label(root, text='Ingrese su patrimonio:')
        self.etiqueta_pat.place(x=20, y=80)
        self.caja_pat = ttk.Entry(root)
        self.caja_pat.place(x=260,y=80, width=100)

        self.etiqueta_est = ttk.Label(root, text='Ingrese su estrato:')
        self.etiqueta_est.place(x=20, y=110)
        self.caja_est = ttk.Entry(root)
        self.caja_est.place(x=260,y=110, width=100)

        self.boton_calcular = ttk.Button(root, text="Calcular matrícula", command=self.calcularMat)
        self.boton_calcular.place(x=130, y=150, width=130)

        self.etiqueta_resultado = ttk.Label(root)
        self.etiqueta_resultado.place(x=20, y=190)
    
    def calcularMat(self):
        ni = self.caja_ni.get()
        nom = self.caja_nom.get()
        pat = int(self.caja_pat.get())
        est = int(self.caja_est.get())
        pagmat = 50000

        if pat > 2000000 and est > 3:
            pagmat = int(pagmat + (pat * 0.03))
            self.etiqueta_resultado.config(text=f'El estudiante con número de inscripción: {ni}\nNombre: {nom}\nDebe pagar ${pagmat}')
        else:
            self.etiqueta_resultado.config(text=f'El estudiante con número de inscripcion: {ni}\nNombre: {nom}\nDebe pagar ${pagmat}')

root = tk.Tk()
root.title("Ejercicio resuelto No 10")
root.config(width=380, height=260)
app = MatriculaU(root)
root.mainloop()