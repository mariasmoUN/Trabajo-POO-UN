""" Ejercicio propuesto No 19,
 Realizado por Mariana Arias Montoya """

import math

# Pedimos el dato del lado del triangulo 
lado = int(input('Ingrese el valor del lado del triangulo: '))

# Calculamos su perimetro
perimetro = 3 * lado # Calculamos su perimetro

# Calculamos su altura
altura = round((math.sqrt(3) / 2) * lado, 3)

# Calculamos su area
area = round((math.sqrt(3) / 4) * lado**2, 3)

print(f'Su perimetro es: {perimetro}, su altura es: {altura} y su area es: {area}')