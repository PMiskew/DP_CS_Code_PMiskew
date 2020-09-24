'''
Name: readFileToList

This function takes a file name as a string and copies the files 
content to a list.  The function returns the list. 

Parameter: String name
Precondition - name is a valid file name
Returns: a list containing all the elements in the file 

'''

def readFileToList(name):

	#open is a function that takes two String parameters and returns 
	#a reference to a file.  Open is in Pythons standard library because
	#I can directly access it. 
	file = open(name,"r")

	#create a new list called result which is empty
	result = []

	#while C.hasNext():
	for line in file:
		result.append(line)

result = readFileToList("data.txt")