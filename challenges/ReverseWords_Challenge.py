"""
Write a function that will take a given string and reverse the order of the words. 
"Hello world" becomes "world Hello" and "May the Fourth be with you" becomes 
"you with be Fourth the May"
"""

a = "hello world. Im amos".split()
b = a[::-1]
print ' '.join(b)
