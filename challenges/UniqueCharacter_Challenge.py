"""
Write a function that determines if any given string379 has all unique 
characters (i.e. no character in the string is duplicated). 
If the string has all unique characters, print "all unique". 
If the string does not have all unique characters, print "duplicates found."
"""

def uniqueCharacters(str):
	list = []
	for i in str: 
		if i in list: 
			print "duplicates found"
			return 
		list.append(i)
	print "all unique"
	
	
uniqueCharacters("soma")
uniqueCharacters("ssoma")		