#Get the product of three biggest integers in an array 
def maxProductFinder(*args):
	sorted_items = sorted(args, reverse=True)
	list_items = []

	for item in sorted_items: 
		list_items.append(item)
		
	print reduce(lambda x, y: x*y, list_items[0:3])
	
maxProductFinder(-8, 6, -7, 3, 2, 1, -9) 
	
	
"""
Given an array of integers, write a function, maxProductFinder, that finds the 
largest product that can be obtained from ANY 3 integers in the array.
"""
def maxProd(x=[]):
	x = sorted(x)
	r1 = x[-1] * x[-2] * x[-3]
	r2 = x[0] * x[1] * x[-1]
	
	return max(r1, r2)
	
print maxProd([-6, -8, 4, 2, 5, 3, -1, 9, 10])
print maxProd([-8, 6, -7, 3, 2, 1, -9])