"""
	- Construye una funcion, changeOptions, que dada una cantidad de dinero y una lista de valores 
	te devuelva todas las posibles combinacion a devolver ese dinero basadas en la lista de valores. 
	- La funcion recibe la cantidad (n), y la lista de valores (s). 
	- n es la cantidad que recibo en dinero 
	- s el cambio que dispongo en la caja 
	
	- P. ej.: 
		changeOptions(5, [1, 2, 5, 10, .., 50000]) => 4
		Las posibilidades de devolucion de 5 euros son 4, estas son: 
			1, 1, 1, 1, 1 
			1, 1, 1, 2
			1, 2, 2
			5 
		
	Se trata de un cajero automatico 
	
	** Solution from cmecklenborg from codeacademy 
	
	
	***
	La memoizacion (memoization) es una tecnica de optimizacion de funciones que consiste 
	en guardar los resultados computados de una funcion para despues volver a usarlos 
	sin necesidad de computarlos de nuevo.
	Guardandolos en la cache por asi decirlo. 
	Ej.: http://www.nakerium.com/foro/viewtopic.php?t=1193
	https://www.sitepoint.com/implementing-memoization-in-javascript/
	Muy util con fibonacci asi no tiene q calcularlo siempre. 
"""

def changeOptions(n, S):
	
	# Controlamos q no se inserte 0 o un numero no valido 
	if n < 0 or n % 1 != 0: 
		return 0 
		
	# Initialize list for memoization
	# Si el valor es 5, la lista tendra 6 de longitud [0,0,0,0,0,0]
	table = [0 for x in range(n + 1)]
	 
	# Initialize base case (n = 0; 1 solution, return no coins)
	# [1,0,0,0,0,0]
	table[0] = 1
	
	# Loop over coins
	for i in range(0, len(S)):
		# Loop over values of n. Number of combinations involving adding the
        # current coin is equal to number of previous combinations for (n-Sj)
		for j in range(S[i], n + 1):
			table[j] += table[j-S[i]]
	
	return table[n]
	
S = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
print changeOptions(5, S)
print changeOptions(26730, S)