"""
1. Write a function, primeNumberDetector, that tests if a number, n is a prime number.
Divisble by himself and 1 
2. Write a function, primeNumberPrinter, that will print out all prime numbers in a given string.
"""
def primeNumberDetector(n): 
	if n < 2: 
		return False 
		
	for i in range(2, n):
		if n % 2 == 0: 
			return False 
			
	return True
	
print "PRIME NUMBER DETECTOR"
print primeNumberDetector(2)
print ("")


def primeNumberPrinter(s): 
	primes = []
	for i in range(len(s)):
		#print s[i] -> devuelve cada letra del string 
		temp = ""
		# and while numbers in string are <= 9 and >= 0 -> ord() transform them into ascii 
		while i != len(s) and ord(s[i]) <= 57 and ord(s[i]) >= 48: 
			# this check for asd123 -> the string 
			# first add the 1 and check if its prime to add him to the list, 
			# then the 12 and check, then 123, then 2, then 2, then 3  
			temp += s[i] 
			if primeNumberDetector(int(temp)): 
				primes.append(int(temp))
			i += 1
	print primes 
	
print "PRIME NUMBER PRINTER"
primeNumberPrinter("asd123")
primeNumberPrinter("asd")
primeNumberPrinter("asd5345kl123o234")



















