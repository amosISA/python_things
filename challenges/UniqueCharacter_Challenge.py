"""
Write a function that determines if any given string has all unique 
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
	
def anotherMethod (stri): 
	bool_check = False
	for i in range(0, len(stri)): 
		for j in range(i+1,len(stri)):
			if stri[i] == stri[j]: 
				bool_check = True
	
	if bool_check: 
		print "duplicates found"
	else: 
		print "all unique"
	
print "UNIQUE WITH FIRST METHOD"
uniqueCharacters("soma")
uniqueCharacters("ssoma")		
uniqueCharacters('==============')
uniqueCharacters('some random string')
uniqueCharacters('abcdefghijklmnopqrstuvwxyz')
uniqueCharacters('12345')
uniqueCharacters('00')
uniqueCharacters('fsa')
uniqueCharacters('fdsa')
uniqueCharacters('ffff')
uniqueCharacters('fadsfasfasdf')
uniqueCharacters('==============')

print "UNIQUE WITH OTHER METHOD:"
anotherMethod("amos")
anotherMethod("amoss")
anotherMethod("aamoss")
anotherMethod("aamos")