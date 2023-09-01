""" Ejercicio resuelto No 11,
 Realizado por Mariana Arias Montoya """

# Declaramos las variables a usar y pedimos su valor por teclado
numA = int(input('Ingrese un numero: '))
numB = int(input('Ingrese un numero: '))
numC = int(input('Ingrese un numero: '))

# Se procede a comparar los valores y a imprimir el mayor valor que corresponda a la condicion
if numA > numB and numA > numC:
    print(f'El valor mayor entre: {numA}, {numB} y {numC} es: {numA}')
elif numB > numA and numB > numC:
    print(f'El valor mayor entre: {numA}, {numB} y {numC} es: {numB}')
else:
    print(f'El valor mayor entre: {numA}, {numB} y {numC} es: {numC}')