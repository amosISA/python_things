"""
Dado un array a una funcion q devuelva los dias q interesa comprar y los q interesa vender. 
Por ejemplo este array de 0 a 7 (son dias): [17, 11, 60, 25, 150, 75, 31, 120]. Compras la accion (profit) q vale 11 el dia 1 (posicion 2 del array)
y la vendes a 150 el dia 4. Luego compras el dia 6 (31) y vendes el dia 7 a 120 por tanto el return seria algo como: [[1, 4],[6, 7]] 
Es decir los arrays dentro del array se componen de: [[dia de compra, dia de venta]] -> Para obtener el maximo beneficio 
Code from ArthurGW codeacademy!
"""

def bestDays(values): 
	# If array has two entries, then only one trade (compraventa) possible, so return it
	# i.e. [2, 60] -> compras el dia 0 y lo vendes el dia 1 
	if len(values) == 2: 
		return [[0, 1]]
	# If array has one or zero entries, no trades possible, return empty list
	elif len(values) == 1 or not values: 
		return [] 
		
	trades = [] # List of trades 
	share = 0 # flag to indicate whether share currently held 
	
	# Recorremos la lista 
	for i in range(len(values)-1): 
	
		if not share: # Share not held 
			if values[i+1] > values[i]: # Increasing tomorrow 
				trades.append([i])
				share = 1
				
		else: # Share held 
			if values[i+1] < values[i]: # Decreasing tomorrow 
				trades[len(trades)-1].append(i) # Add sell day to existing trade
				share = 0
				
	# If share held on last day, sell 
	if share: 
		trades[len(trades)-1].append(len(values)-1)
		
	elif not trades: # No share held, no trades made, the result of decreasing array
		# Find day with minium loss: 
		buy = min(range(len(values)-1), key=lambda i: values[i]-values[i+1])
		return [[buy, buy + 1]] # Sell on next day 
		
	return trades 
			
		
print bestDays([17, 11, 60, 25, 150, 75, 31, 120])
print bestDays([90, 170, 250, 300, 30, 525, 685, 90])
print bestDays([10, 7, 6, 3, 1])
print bestDays([5, 4, 3, 2, 1])
print bestDays([5,2,4])
print bestDays([5,9,4])
print bestDays([43,2])
print bestDays([2,43])
print bestDays([43])
print bestDays([])