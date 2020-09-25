'''
Description: 

Write a method called reverseWordA.  The method takes a Strings and returns 
the string in reverse 


Name: reverseWordA
Parameters: String s
Returns: String

Precondition: s is a valid string of any length.

reverseWordA(“cat”) → “tac”

'''

def reverseWordA(s):

	a = "" #empty string that I will build the result with

	#loop through the stirng in reverse
	for i in range(len(s) - 1, -1, -1):

		a = a + s[i]

	return a

print(reverseWordA(""))



