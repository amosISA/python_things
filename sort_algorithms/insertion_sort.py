"""
Insertion Sort 
Aqui a partir de la lista de elementos a ordenar se crea otra lista interna 
donde se van anadidendo los items de la lista a ordenar de menor a mayor 
"""

def insertionSort(list): 
	for i in range(1, len(list)):
		j = i 
		while j > 0 and list[j] < list[j-1]: 
			list[j], list[j-1] = list[j-1], list[j]
			j -= 1
	return list 
	
print insertionSort([234, 654, 786, 234, 234, 2])