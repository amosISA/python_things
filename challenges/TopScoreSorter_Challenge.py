"""
You've spent decades setting high scores on Donkey Kong but now, 
a challenger approaches. Write a function, scoreSettler, that will 
definitively show who is the King of Kong. scoreSettler will take 
a list of unsorted scores plus the highest possible score and return 
a sorted list of all of the scores, in descending order from high 
score to low score.
"""

scorelist = [874300, 879200, 1172100, 1141800, 933900, 1177200, 1190200, 1110100, 1158400, 985600, 1047200, 1049100, 1138600, 1170500, 1064500, 1190000, 1050200, 1090400, 1062800, 1061700, 1218000, 1068000, 1127700, 1144800, 1195100]
scoremax = 1218000

def scoreSettler(list, max):
	scores = []	
	[scores.append(x) for x in list if list > 0 and x < max]
	print scores[::-1] 
	
scoreSettler(scorelist, scoremax)