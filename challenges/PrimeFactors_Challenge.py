from math import sqrt 

list = []
def primeFactor(n):
	if n > 1: 
		# Divide by 2 /// 100 / 2 = 50 /// 50 / 2 = 25 === 2, 2
		while n % 2 == 0: 
			list.append(2)
			n = n / 2
			
		# When exits first while n = 25 
			
		# When you cant divide by 2, you divide by next highest number, 3, and so on (i += 2), 5, 7 ... 
		i = 3
		while i <= sqrt(n): 
			while n % i == 0: # 25 / 5 = 5 /// 5 / 5 = 1   === 2, 2, 5, 5 
				list.append(i)
				n = n / i 
			i += 2
				
		# Here n = 1
			
		# If some number got his last prime factor such as 797, this will be added to the list as his last 
		# (example prime factors of 9564)
		if n > 2:
			list.append(n);
				
		print list
	else: 
		print "Number should be higher than 1"
		
def primeFactorSum(list_n): 
	values = 0 
	for i in list_n: 
		values += i 
	return values 
	
def uniquePrimeFactors(list_n):
	my_list = []
	for i in list_n: 
		if i not in my_list: 
			my_list.append(i)
	return my_list 
	
print "Prime factors:"
primeFactor(100)
print "Sum of prime factors are:"	
print primeFactorSum(list)	
print "Unique prime factors:"
print uniquePrimeFactors(list)	