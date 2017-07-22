"""
Escribe una funcion, getX, q dado un entero x y una lista devuelva el x numero
si la lista estaba ordenada. Es decir la funcion sera algo asi getX(2, [5,10,-3,7,9]) 
y devolvera 5 pues la lista ordenada es [-3, 5, 7, 9, 10] y 5 esta en la posicion 2 q 2 
es el primer parametro de la funcion para decir q valor queremos obtener de la lista. 
Atencion -> aqui la lista empieza por el index 1 y no por el 0. 
"""

def insertionSort(list): 
	for i in range(1, len(list)): 
		j = i 
		while j > 0 and list[j] < list[j-1]: 
			list[j], list[j-1] = list[j-1], list[j]
			j -= 1 
	return list 

def getX(i, lst):
	if i > len(lst) or i < 1:
		return 'ValueError'
		
	# aqui para obtener el de la posicion a m le asignamos el minimo de la lista y lo vamos 
	# removiendo, y al final m vale el ultimo valor a remover q es la posicion q queremos 
	# imprimir de la lista 
	for n in range(i): 
		m = min(lst)
		lst.remove(m)
	
	return m 
	
def getXSorted(i, lst): 
	if i > len(lst) or i < 1:
		return 'ValueError'
		
	sorted_lst = insertionSort(lst)
	
	for j in range(len(sorted_lst)):
		if j == i:
			print sorted_lst[j-1]

print "With sorted algorithm: "
getXSorted(4, [5,10,-3,7,9]) 
getXSorted(2, [5,10,-3,7,9])
getXSorted(10, [5,10,-3,7,9,234,654,-234,234,978,6,7])
print("")

print "Without sorting:"
print getX(4, [5,10,-3,7,9]) 
print getX(2, [5,10,-3,7,9])
print getX(10, [5,10,-3,7,9,234,654,-234,234,978,6,7])