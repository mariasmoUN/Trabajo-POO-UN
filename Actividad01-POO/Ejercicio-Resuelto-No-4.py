""" Ejercicio Resuelto No 4 """
""" Realizado por Mariana Arias Montoya """

ageJuan = int(input('Ingrese la edad de Juan: '))

ageAlberto = 2*(ageJuan/3)
ageAna = 4*(ageJuan/3)
ageMama = ageAlberto + ageJuan + ageAna

print(f'La edades son: Alberto: {int(ageAlberto)}, Juan: {ageJuan}, Ana: {int(ageAna)}, Mama: {int(ageMama)}')