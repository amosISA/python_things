
# 1. Fibonacci de forma recursiva, no es muy util pues tarda bastante, y ademas se recomienda no buscar por encima de 20 

count = 0

def fibonacci(n): 
	global count
	count += 1
	
	if(n < 3):
		return 1 
	
	return fibonacci(n - 1) + fibonacci(n - 2)

a = fibonacci(10)
print "It took "+str(count)+" calculations to find that the 10th fibonacci number is "+str(a)+"."
		
		
"""
2. Write a function, fibonacciFinderN, that will find the nth number in the Fibonacci Sequence.
In the Fibonacci Sequence, the first two numbers are 0 and 1 and every number thereafter is the sum of the previous two numbers in the sequence
"""
def fibonacciFinderN(n): 
	
	# if n < 1, n is rejected 
	if n < 1: 
		return 
		
	# if n == 1, 0 is returned right away because the initial of x, y, z already 
	# move the sequence past n == 1 
	if n == 1: 
		return 0 
		
	x = 0 # first number of sequence 
	y = 1 # second 
	z = 1 # third 
	i = 3 
	
	# Here the while loop will do a single pass for 1-n, while accumulating the fibonacci number
    # and thus making the algorithm directly proportional with the size of n.
    # This makes the time complexity O(n).
	
	while i <= n: 
		z = x + y 
		x = y   
		y = z 
		
		i += 1 
		
	return z
	
print fibonacciFinderN(5)	
print fibonacciFinderN(300)
		