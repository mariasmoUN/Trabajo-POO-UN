""" Ejercicio propuesto No 12,
 Realizado por Mariana Arias Montoya """

hTrabajadas = int(input('Ingrese el total de horas trabajadas en la semana: '))
valorHora = 5000

salarioB = valorHora * hTrabajadas #se hace el cálculo del salario bruto
retencion = int(salarioB * 0.125) #se calcula la retencion en la fuente teniendo en cuenta el salario bruto
salarioN = salarioB - retencion # se calcula el salario neto restando la retencion en la fuente

print(f'El salario bruto es de ${salarioB}, la retencion en la fuente es de ${retencion}, y el salario neto es de ${salarioN}.')