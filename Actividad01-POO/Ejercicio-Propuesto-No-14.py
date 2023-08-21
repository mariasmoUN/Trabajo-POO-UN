""" Ejercicio propuesto No 14,
 Realizado por Mariana Arias Montoya """

import math #importamos la librería math para algunos cálculos

num = int(input('Ingrese un numero: '))

cuadrado = int(math.pow(num, 2)) #calculamos el valor de su cuadrado
cubo = int(math.pow(num, 3)) #calculamos el valor de su cubo

print(f'El cuadrado y el cubo del numero {num} es: {cuadrado} y {cubo}')