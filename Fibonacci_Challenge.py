count = 0

def fibonacci(n): 
	global count
	count += 1
	
	if(n < 3):
		return 1 
	
	return fibonacci(n- 1) + fibonacci(n - 2)

a = fibonacci(10)
print "It took "+str(count)+" calculations to find that the 10th fibonacci number is "+str(a)+"."
		