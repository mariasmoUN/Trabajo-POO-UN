""" Ejercicio resuelto No 7,
 Realizado por Mariana Arias Montoya """

import tkinter as tk

class Comparador:
    def __init__(self, root):
        
        self.etiqueta_a = tk.Label(root, text="Ingrese el valor de A:")
        self.etiqueta_a.place(x=20, y=20)
        self.caja_a = tk.Entry(root)
        self.caja_a.place(x=160, y=20, width=100)
        
        self.etiqueta_b = tk.Label(root, text="Ingrese el valor de B:")
        self.etiqueta_b.place(x=20, y=60)
        self.caja_b = tk.Entry(root)
        self.caja_b.place(x=160, y=60, width=100)
        
        self.comparar_boton = tk.Button(root, text="Comparar", command=self.comparar_ab)
        self.comparar_boton.place(x=90, y=100, width=100)

        self.etiqueta_resultado = tk.Label(root)
        self.etiqueta_resultado.place(x=20, y=140)
    
    def comparar_ab(self):
 
        a = int(self.caja_a.get())
        b = int(self.caja_b.get())
        
        if a > b:
            resultado = 'A es mayor a B'
        elif a == b:
            resultado = 'A es igual a B'
        else:
            resultado = 'A es menor a B'
        
        self.etiqueta_resultado.config(text=resultado)

root = tk.Tk()
root.title("Ejercicio resuelto No 7")
root.config(width=280, height=180)
app = Comparador(root)
root.mainloop()