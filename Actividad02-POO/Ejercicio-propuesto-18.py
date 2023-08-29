""" Ejercicio propuesto No 18,
 Realizado por Mariana Arias Montoya """

# Información del empleado:
codigoEmpl = input('Ingrese el código del empleado: ')
name = input('Ingrese el nombre del empleado: ')
horasTrab = int(input('Ingrese el total de horas trabajadas al mes: '))
valorHora = 5000
porRetencion = 0.015

# Calculamos el salario bruto:
salarioB = horasTrab * valorHora

# Calculamos el salario neto, primero calculamos la retencion
retencion = int(salarioB * porRetencion)
salarioN = salarioB - retencion


print(f'{codigoEmpl} - {name} - {salarioB} - {salarioN}')
