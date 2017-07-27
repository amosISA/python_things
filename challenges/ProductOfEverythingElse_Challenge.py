"""
Escribe una funcion, productOfTheOthers que, dado un array de enteros, reemplaze cada 
numero en el array por el producto de todos los demas numeros excepto el mismo. 
Es decir: dado el sigueinte array: [1,2,3,4] q me de ->  [24, 12, 8, 6]
Esto es, en la primer iteracion q es 1 me da 24 pq multiplica 2 * 3 * 4 y para la 
segunda multiplica 1 * 3 * 4, asi... lo multiplica por todos los demas menos por si mismo. 
"""

def productOfTheOthers(list): 
	product = 1 
	output = []
	for i in range(0, len(list)):
		for j in range(0, len(list)):
			if list[i] != list[j]: 
				product *= list[j] 
		output.append(product)
		product = 1
		
	return output 
		
print productOfTheOthers([1, 2, 3, 4])