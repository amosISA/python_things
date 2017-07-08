#Get the product of three biggest integers in an array 
def maxProductFinder(*args):
	sorted_items = sorted(args, reverse=True)
	list_items = []

	for item in sorted_items: 
		list_items.append(item)
		
	print reduce(lambda x, y: x*y, list_items[0:3])
	
maxProductFinder(-8, 6, -7, 3, 2, 1, -9) 
	