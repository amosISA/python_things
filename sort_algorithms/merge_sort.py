"""
Merge Sort, el quick sort es parecido 
Se va resquebrajando la lista en listas diminutas mediante la recursividad 
"""

def mergeSort(list):
	if len(list) > 1: 
		mid = len(list) / 2 # partimos en dos la lista y obtenemos dos listas: left y right 
		left = list[0:mid]
		right = list[mid:]
		
		# volvemos a partir las dos listas mediante la recursividad 
		mergeSort(left)
		mergeSort(right)
		
		l, r = 0, 0 
		
		for i in range(len(list)): 
			lval = left[l] if l < len(left) else None 
			rval = right[r] if r < len(right) else None

			if (lval and rval and lval < rval) or rval is None:
				list[i] = lval
				l += 1
			elif (lval and rval and lval >= rval) or lval is None:
					list[i] = rval
					r += 1
			else: 
				raise Exception('Could not merge, sub arrays sizes do not match the main array')
		
	return list
	
print mergeSort([234, 432, 23, 2, 34])