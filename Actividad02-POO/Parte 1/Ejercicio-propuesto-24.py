""" Ejercicio propuesto No 24,
 Realizado por Mariana Arias Montoya """

# Pedimos los siguientes valores por teclado:
A = int(input('Ingrese el peso de la esfera A: '))
B = int(input('Ingrese el peso de la esfera B: '))
C = int(input('Ingrese el peso de la esfera C: '))

# Hacemos los condicionales para buscar la de mayor peso

if A > B and A > C:
    print('A es la de mayor peso')
elif B > A and B > C:
    print('B es la de mayor peso')
else:
    print('C es la de mayor peso')