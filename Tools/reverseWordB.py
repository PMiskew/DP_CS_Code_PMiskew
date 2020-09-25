'''
Description: 

Write a method called reverseWordB.  The method takes a list of Strings 
and returns a new string of each word constructed in reverse.  


Name: reverseWordB
Parameters: String[] s
Returns: String

Precondition: s is a list of any length and it contains strings 
of any length

reverseWordB({“cat”,”dog”}) → “tacgod”
'''
def reverseWordB(s):

	a = ""
	#First loop will go through the elemetns in s
	for i in range(0, len(s), 1):
		
		word = s[i]

		for j in range(len(word) - 1, -1, -1):
			a = a + word[j]


	return a


a = ["cat","dog"]
print(reverseWordB(a))


