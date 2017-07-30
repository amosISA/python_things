# Write a function, isPermPalindrome, that will test if a given string is a permutation of a palindrome.
import collections 

def isPermPalindrome(pal):
	oddCount = 0 # graba el numero de veces q una letra aparece como impar 
	strList = ''.join(char.lower() for char in pal if char.isalnum()) # kayak 
	alphaCount = collections.Counter(strList) # { 'a':2, 'k':2, 'y':1} -> cuenta las veces q se repite una letra, es un dict 
	
	for c in alphaCount.values():
		if (c % 2 == 1): # si los valores de las letras del dict son impares se suma 1 a la variable 
			oddCount = oddCount + 1
			
	if (len(pal) % 2 == 0): # amos -> entra aqui, como todas son impares, devuelve False 
		if (oddCount == 0):
			return True 
		else: 
			return False 
	else: # amo -> pero aqui oddCount seria 3, no uno, devuelve False, Kayak devolveria true 
		if(oddCount == 1):
			return True 
		else: 
			return False 
	
print isPermPalindrome('Kayak')
print isPermPalindrome('No lemon, no melon')
print isPermPalindrome('No, lemon no melon')
print isPermPalindrome('amos')
print isPermPalindrome('amo')