""" Ejercicio resuelto No 13,
 Realizado por Mariana Arias Montoya """

# Se definen las variables y se piden valores por teclado
vCompra = int(input('Ingrese el valor total de su compra: '))
colorB = input('Ingrese el color de la bolita que saco: ')

# Se inicia el ciclo para comparar el color de la bolita con el respectivo descuento
if colorB == 'blanco':
    print(f'El cliente debe pagar: ${vCompra}')
elif colorB == 'verde':
    descuento = int(vCompra * 0.1)
    vPagar = vCompra - descuento
    print(f'El cliente debe pagar: ${vPagar}')
elif colorB == 'amarilla':
    descuento = int(vCompra * 0.25)
    vPagar = vCompra - descuento
    print(f'El cliente debe pagar: ${vPagar}')
elif colorB == 'azul':
    descuento = int(vCompra * 0.5)
    vPagar = vCompra - descuento
    print(f'El cliente debe pagar: ${vPagar}')
else:
    print(f'El cliente debe pagar: $0')