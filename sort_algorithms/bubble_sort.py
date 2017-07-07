"""
Bubble Sort
Se asemeja a las burbujas de una bebida. Los valores de menos peso se quedan 
al principio y los de mas peso al final. Por tanto se ordena la lista de menor a mayor. 
Aqui se empieza por el primer item de la lista y va comparandolos con los demas y si es mayor
lo va arrastrando hasta el final. 

Outer loop: i = 0 to n-1 
Inner llop: j = 0 to n-1-i -> pq sabemos q el ultimo ya esta ordenado 
"""
def bubbleSort(myList): 
	# Primer for coge todos menos el ultimo 
	for i in range(0, len(myList) - 1):
		for j in range(0, len(myList) - 1 - i):
			# Aqui comparamos el item con el de su derecha sin coger el ultimo 
			# ni el ya recorrido en el primer for (i)
			if myList[j] > myList[j+1]:
				myList[j], myList[j+1] = myList[j+1], myList[j] #swap values 
	return myList 
	
def optimizedBubbleSort(myList): 
	update = True 
	n = len(myList)
	
	while(update == True and n > 1): 
		update = False 
		for i in range(len(myList) - 1): 
			if myList[i] > myList[i+1]: 
				myList[i] ,myList[i+1] = myList[i+1], myList[i]
				update = True
		n -= 1
	return myList 
				
print "BubbleSort"
print bubbleSort([123, 54, 234, 765, 876])
print "Optimized BubbleSort"
print optimizedBubbleSort([123, 54, 234, 765, 876])