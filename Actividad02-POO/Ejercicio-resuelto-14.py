""" Ejercicio resuelto No 14,
 Realizado por Mariana Arias Montoya """

# Pedimos los siguientes datos por teclado:
departamentoA = int(input('Ingrese el importe de ventas del departamento 1: '))
departamentoB = int(input('Ingrese el importe de ventas del departamento 2: '))
departamentoC = int(input('Ingrese el importe de ventas del departamento 3: '))
salario = int(input('Ingrese el salario de los vendedores: '))

# Se hacen algunos calculos de interés:
totalVent = departamentoA + departamentoB + departamentoC
porcentajeVent = 0.33 * totalVent

if departamentoA > porcentajeVent:
    salarioA = int(salario + (0.2 * salario))
else:
    salarioA = salario

if departamentoB > porcentajeVent:
    salarioB = int(salario + (0.2 * salario))
else:
    salarioB = salario

if departamentoC > porcentajeVent:
    salarioC = int(salario + (0.2 * salario))
else:
    salarioC = salario

print(f'Salario de vendedores del departamento 1: ${salarioA}, Salario de vendedores del departamento 2: ${salarioB}, Salario de vendedores del departamento 3: ${salarioC},')