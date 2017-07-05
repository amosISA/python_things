"""
Write a function that finds the sum of all prime factors of a given number, n.
Do it without using Trial Division (division por tentativa): An individual integer 
being tested is called a trial divisor.
This exercises is from codeplayer75939 in codeacademy. Not mine. 
"""
from math import sqrt
#this function will sum the primes found:
def sum(list):
  values=0
  for i in list:
    values+=i
  print values
  return values

#This function will find the primes in a number n:
primes=[]
def findprimes(n):
  while n%2==0:                 #if our number n is even it will append a 2 factor and it will be divided until we get an odd number.
    primes.append(2) 
    n=n/2
  i=3
  while i<=sqrt(n):             #The tiniest prime factor of a number n must be equal or less than its square root. We add them while
    while n%i==0:               #dividing it, so it will append every factor until we have the last factor (irreducible).
      primes.append(i)
      n=n/i
    i+=2
  if n>2:                          #Here we append the last factor.
    primes.append(n)
  
findprimes(3072)
print "The list of primes is: "
print primes
print "And their sum is: "
+sum(primes)

#the next function filters the repeated primes:
def sumdifferentprimes(list):
  newlist=[]
  for item in list:            #Basically it adds a number unless it was already added.
    if item not in newlist:
      newlist.append(item)
  newsum=0
  for i in newlist:
    newsum+=i
  print newlist
  print newsum
  return newsum
print "The list with no repetitions and the sum:"
sumdifferentprimes(primes)

