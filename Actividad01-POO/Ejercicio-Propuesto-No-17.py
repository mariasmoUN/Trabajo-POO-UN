""" Ejercicio propuesto No 17,
 Realizado por Mariana Arias Montoya """

import math #importamos la librería math para algunos cálculos

radio = int(input('Ingrese el valor del radio del circulo: '))
area = round(math.pi * (radio**2), 3) #calculamos el area con la formula de π*r²
longCircunferencia = round(2 * math.pi * radio, 3) #longitud de la circunferencia con la formula 2(π*r) 

print(f'El area del circulo es {area} y la longitud de su circunferencia es {longCircunferencia}')