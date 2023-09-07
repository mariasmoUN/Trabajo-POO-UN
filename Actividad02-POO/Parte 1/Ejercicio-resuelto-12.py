""" Ejercicio resuelto No 12,
 Realizado por Mariana Arias Montoya """

# Declaramos las variables a usar y pedimos su valor por teclado
name = input('Ingrese el nombre del trabajador: ')
hTrabajadas = int(input('Ingrese el total de horas trabajadas en la semana: '))
vHora = int(input('Ingrese el valor de la hora de trabajo: '))

# Se inicia el ciclo verificando que el total de horas sea mayor o menor a 40
if hTrabajadas > 40:
    hExtra = hTrabajadas - 40

    # en caso de que se exceda de las 40 horas se verifica si estas son mayores o menores a 8
    if hExtra > 8:
        hExtraExcedida = hExtra - 8
        salario = 40 * vHora + 16 * vHora + hExtraExcedida * 3 * vHora
        print(f'El trabajador {name} devengo ${salario}')
    else:
        salario = 40 * vHora + hExtra * 2 * vHora
        print(f'El trabajador {name} devengo ${salario}')
else:
    salario = hTrabajadas * vHora
    print(f'El trabajador {name} devengo ${salario}')