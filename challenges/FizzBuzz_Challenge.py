"""
Write a program that prints the numbers from 1 to 100. But for 
multiples of three print Fizz instead of the number and for 
the multiples of five print Buzz. For numbers which are multiples 
of both three and five print FizzBuzz.
"""
for i in range(101): 
	# if number is divisible by 5 or 3 prints FizzBuzz
	if i % 3 == 0 and i % 5 == 0:
		print "Fizz"   
	# if number is divisible by 5 prints Buzz
	elif i % 5 == 0: 
		print "Buzz"
	# if number is divisible by 3 prints Fizz
	elif i % 3 == 0:
		print "FizzBuzz"  
	else: 
		print i 