z = 1
odd_numbers = []

def timesTables():
	global z, odd_numbers
	for i in range(1, 13):
		print z * i,

		if z*i % 2 != 0:
			odd_numbers.append(z*i) 
		
	print ''
	z += 1

while(z!=13):
	timesTables()

print odd_numbers
