""" Ejercicio propuesto No 22,
 Realizado por Mariana Arias Montoya """

# Pedimos los siguientes datos por teclado:
name = input('Ingrese el nombre del trabajador: ')
salarioH = int(input('Ingrese el salario basico por hora: '))
horasT = int(input('Ingrese el total de horas trabajadas al mes: '))

# Calculamos su salario mensual en relación a las horas trabajadas
salarioM = salarioH * horasT

# Comparamos si su salario es mayor o menor al indicado
if salarioM > 450000:
    print(f'{name} - {salarioM}')
else:
    print(name)