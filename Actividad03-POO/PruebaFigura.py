import tkinter as tk
from tkinter import ttk

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return 3.14159265359 * self.radio * self.radio

    def calcularPerimetro(self):
        return 2 * 3.14159265359 * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado

    def calcularPerimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return 0.5 * self.base * self.altura

    def calcularPerimetro(self):
        return self.base + self.altura + (self.base ** 2 + self.altura ** 2) ** 0.5

    def determinarTipoTriangulo(self):
        if self.base == self.altura:
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")

if __name__ == "__main__":
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3, 5)

def calcular_resultados():
    radio = float(entry_radio.get())
    base = float(entry_base.get())
    altura = float(entry_altura.get())
    lado = float(entry_lado.get())

    figura1 = Circulo(radio)
    figura2 = Rectangulo(base, altura)
    figura3 = Cuadrado(lado)
    figura4 = TrianguloRectangulo(base, altura)

    label_resultado_circulo.config(text="El area del circulo es = {:.2f}".format(figura1.calcularArea()))
    label_resultado_perimetro_circulo.config(text="El perimetro del circulo es = {:.2f}".format(figura1.calcularPerimetro()))

    label_resultado_rectangulo.config(text="El area del rectangulo es = {:.2f}".format(figura2.calcularArea()))
    label_resultado_perimetro_rectangulo.config(text="El perimetro del rectangulo es = {:.2f}".format(figura2.calcularPerimetro()))

    label_resultado_cuadrado.config(text="El area del cuadrado es = {:.2f}".format(figura3.calcularArea()))
    label_resultado_perimetro_cuadrado.config(text="El perimetro del cuadrado es = {:.2f}".format(figura3.calcularPerimetro()))

    label_resultado_triangulo.config(text="El area del triangulo es = {:.2f}".format(figura4.calcularArea()))
    label_resultado_perimetro_triangulo.config(text="El perimetro del triangulo es = {:.2f}".format(figura4.calcularPerimetro()))

    figura4.determinarTipoTriangulo()
    label_resultado_tipo_triangulo.config(text="Tipo de triángulo: " + figura4.tipo_triangulo)

root = tk.Tk()
root.title("Calculadora de Figuras Geométricas")

label_radio = ttk.Label(root, text="Radio:")
entry_radio = ttk.Entry(root)

label_base = ttk.Label(root, text="Base:")
entry_base = ttk.Entry(root)

label_altura = ttk.Label(root, text="Altura:")
entry_altura = ttk.Entry(root)

label_lado = ttk.Label(root, text="Lado:")
entry_lado = ttk.Entry(root)

calcular_button = ttk.Button(root, text="Calcular", command=calcular_resultados)

label_resultado_circulo = ttk.Label(root, text="")
label_resultado_perimetro_circulo = ttk.Label(root, text="")

label_resultado_rectangulo = ttk.Label(root, text="")
label_resultado_perimetro_rectangulo = ttk.Label(root, text="")

label_resultado_cuadrado = ttk.Label(root, text="")
label_resultado_perimetro_cuadrado = ttk.Label(root, text="")

label_resultado_triangulo = ttk.Label(root, text="")
label_resultado_perimetro_triangulo = ttk.Label(root, text="")
label_resultado_tipo_triangulo = ttk.Label(root, text="")

label_radio.grid(row=0, column=0, padx=5, pady=5)
entry_radio.grid(row=0, column=1, padx=5, pady=5)

label_base.grid(row=1, column=0, padx=5, pady=5)
entry_base.grid(row=1, column=1, padx=5, pady=5)

label_altura.grid(row=2, column=0, padx=5, pady=5)
entry_altura.grid(row=2, column=1, padx=5, pady=5)

label_lado.grid(row=3, column=0, padx=5, pady=5)
entry_lado.grid(row=3, column=1, padx=5, pady=5)

calcular_button.grid(row=4, columnspan=2, padx=5, pady=5)

label_resultado_circulo.grid(row=5, columnspan=2, padx=5, pady=5)
label_resultado_perimetro_circulo.grid(row=6, columnspan=2, padx=5, pady=5)

label_resultado_rectangulo.grid(row=7, columnspan=2, padx=5, pady=5)
label_resultado_perimetro_rectangulo.grid(row=8, columnspan=2, padx=5, pady=5)

label_resultado_cuadrado.grid(row=9, columnspan=2, padx=5, pady=5)
label_resultado_perimetro_cuadrado.grid(row=10, columnspan=2, padx=5, pady=5)

label_resultado_triangulo.grid(row=11, columnspan=2, padx=5, pady=5)
label_resultado_perimetro_triangulo.grid(row=12, columnspan=2, padx=5, pady=5)
label_resultado_tipo_triangulo.grid(row=13, columnspan=2, padx=5, pady=5)

root.mainloop()