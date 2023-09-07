""" Ejercicio propuesto No 21,
 Realizado por Mariana Arias Montoya """

import math

# Tomamos los valores de sus lados 
a = int(input('Ingrese el valor del primer lado: '))
b = int(input('Ingrese el valor del segundo lado: '))
c = int(input('Ingrese el valor del tercer lado: '))

# Calculamos el perimetro:
perimetro = a + b + c

# Calculamos el semiperimetro:
p = perimetro/2

# calculamos el área utilizando la fórmula de Herón
area = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 3)

print(f'El perimetro es: {perimetro}, el semiperimetro es: {p} y su area es: {area}')