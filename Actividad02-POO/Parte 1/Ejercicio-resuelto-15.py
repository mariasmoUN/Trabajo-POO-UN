""" Ejercicio resuelto No 15,
 Realizado por Mariana Arias Montoya """

# Pedimos los pesos de las esferas por teclado
pesoA = int(input('Ingrese el peso de la esfera A: '))
pesoB = int(input('Ingrese el peso de la esfera B: '))
pesoC = int(input('Ingrese el peso de la esfera C: '))
pesoD = int(input('Ingrese el peso de la esfera D: '))

# Realizamos las comparaciones
if (pesoA == pesoB) and (pesoA == pesoC):
    if pesoA < pesoD:
        print('La esfera D es la diferente y es de mayor peso')
    else:
        print('La esfera D es la diferente y es de menor peso')
elif (pesoA == pesoB) and (pesoA == pesoD):
    if pesoA < pesoC:
        print('La esfera C es la diferente y es de mayor peso')
    else:
        print('La esfera C es la diferente y es de menor peso')
elif (pesoA == pesoC) and (pesoA == pesoD):
    if pesoA < pesoB:
        print('La esfera B es la diferente y es de mayor peso')
    else:
        print('La esfera B es la diferente y es de menor peso')
else:
    if pesoB < pesoA:
        print('La esfera A es la diferente y es de mayor peso')
    else:
        print('La esfera A es la diferente y es de menor peso')