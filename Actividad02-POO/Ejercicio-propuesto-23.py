""" Ejercicio propuesto No 23,
 Realizado por Mariana Arias Montoya """

# Usamos la forma Ax^2 + Bx + C = 0
import math

# Pedimos los siguientes datos por teclado:
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

D = B**2 - 4*A*C

if D > 0:
    x1 = (-B + math.sqrt(D)) / (2*A)
    x2 = (-B - math.sqrt(D)) / (2*A)
    print(f"Las soluciones son: x1 = {x1}, x2 = {x2}")
else:
    x = -B / (2*A)
    print(f"La solución doble es: x = {x}")