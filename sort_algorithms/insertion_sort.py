"""
Insertion Sort 
Como funciona? 
Imagina la siguiente lista: [5, 3, 4, 7, 2, 8, 6]
El 5, la posicion 0 se considera como otra lista q ya esta ordenada por tanto se empieza 
en el bucle for por el indice 1 q en nuestro caso es el 3 y se compara el 3 con los numeros 
de la lista ya ordenada ([5]). Por tanto al ser el 3 menor q el 5 se intercambian la posicion, 
ahora la lista ordenada ya tiene [3, 5] y hay q seguir comparando los otros numeros con esta lista 
hasta conseguir la lista ordenada!!! Los numeros q se mueven a la lista ordenada son considerados 
fully sorted y ya no se mueven! 
"""

def insertionSort(list): 
	for i in range(1, len(list)):
		j = i 
		# el j -= 1 esta para q si la lista ordenada tiene varios numeros q los vaya comparando 
		# a todos con el correspondiente p. ejemplo [5, 6, 2], si j esta en la posicion 2 es decir 
		# list[j] seria 2 entonces si lo compara con 6 se hace el swap y j pasa a valer j -= 1 
		# para q de este modo compare de nuevo el 2 con el 5 y por tanto j vale 1 !! asi hasta q salga del while 
		while j > 0 and list[j] < list[j-1]: 
			list[j], list[j-1] = list[j-1], list[j]
			j -= 1
	return list 
	
print insertionSort([234, 654, 786, 234, 234, 2, -55])