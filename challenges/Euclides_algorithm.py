"""
Con su algoritmo encontramos el maximo comun divisor de dos numeros (MCD). 
Por ejemplo de 1112 y 695 tendriamos q factorizarlos y obtendriamos: 
1112 -> 139 x 2 x 2 x 2 
695 = 139 x 5 
Por tanto el MCD de los dos es 139 pero hacerlo asi como mayores sean los numeros 
mas dificil sera la factorizacion por eso entra aqui en juego Euclides: 
Aqui lo q hacemos es dividir el mayor numero entre el mas pequeno asi: 
1112 / 695 = 417 
695 / 417 = 278 
417 / 278 = 139 
278 / 139 = 0 
139 ... MCD 
"""

def gcd(x, y):
    while y != 0:
		# x = 1112, y = 695 => x = y // y = x % y 
		# x = 695, y = 417 
		# x = 417, y = 278 
		# x = 278, y = 139
		# x = 139 
        (x, y) = (y, x % y)
    return x 
			
print gcd(1112, 695)
print gcd(12312, 543)