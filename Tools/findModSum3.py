'''
Description: 

Write a method called findModSum3.  The method takes a list of integers and
two integer values.  The method returns the sum of all the elements that are 
multiples of a and b. 

Name: findModSum3
Parameters: int[] data, int a, int b
Returns: int

Precondition: values is a list of integers of any size and a and b are 
valid positive integer values. 

findModSum({21,30,10,99,14,2,100},5,2) → 30 + 10 + 100 = 140

'''

def findModSum3(data, a, b):

	sum = 0

	for i in range(0, len(data), 1):

		if (data[i] % a == 0 and data[i] % b == 0):

				sum = sum + data[i]

	return sum

a = [21,30,10,99,14,2,100]
print(findModSum3(a,5,2))


















