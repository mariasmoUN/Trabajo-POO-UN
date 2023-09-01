""" Ejercicio resuelto No 10,
 Realizado por Mariana Arias Montoya """

#Declaramos las variables y pedimos los datos de entrada
ni = input('Ingrese el numero de inscripcion: ')
nom = input('Ingrese su nombre: ')
pat = int(input('Ingrese su patrimonio: '))
est = int(input('Ingrese su estrato: '))
pagmat = 50000

#Se inicia un ciclo condicional para comparar el patrimonio y el estrato 
if pat > 2000000 and est > 3:
    pagmat = int(pagmat + (pat * 0.03))
    print(f'El estudiante con numero de inscripcion {ni} y nombre {nom} debe pagar {pagmat}')
else:
    print(f'El estudiante con numero de inscripcion {ni} y nombre {nom} debe pagar {pagmat}')