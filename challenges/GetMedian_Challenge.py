"""
Escribe una funcion, getMedian, q devuelva el valor medio de una lista de numeros. 
Es decir, primero habria q ordenar la lista y luego ver que valor esta en el medio es decir, 
de [-3, 2, 3, 3, 5, 6, 9, 10, 10, 12, 18] es 6 pq esta en el medio. 
"""

def bubbleSort(list): 
	for i in range(0, len(list) - 1):
		for j in range(0, len(list) - 1 - i):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
	return list 

def getMedian(list): 
	newList = bubbleSort(list)
	
	if len(newList) % 2 != 0: # odd list (lista impar)
		# al ser la lista impar quiero q de newList me devuelva el numero con index(lista/2) 
		return newList[(len(newList)/2)]
	else: # even list (lista par)
		# al ser la lista par se devuelve el promedio de los dos valores medianos 
		return (newList[(len(newList)/2)] + newList[(len(newList)/2)-1]) / 2.0 
		
print getMedian([6,10,2,5,9,3,10,12,18,-3]) # aqui la lista al ser par coge los dos del medio, los suma y los divide para obtener el promedio 
print getMedian([5,10,-3,7,9]) # este ordenado seria [-3, 5, 7, 9, 10] -> devuelve 7 al ser el del medio y la lista impar 