""" Ejercicio Resuelto No 5,
 Realizado por Mariana Arias Montoya """

import math # importamos la librería math para algunos cálculos

# Se declaran las variables dadas a utilizar y se piden los valores para X y Y
suma = 0
x = int(input('Ingrese un valor para x: '))
y = int(input('Ingrese un valor para y: '))

# Se cambian las variables suma y x por sus nuevos valores
suma = suma + x
x = x + math.pow(y, 2)

# Sobre la variable suma se hace la operación matemátia indicada 
suma = suma + (x/y)

print(f'La suma es: {suma}')