'''
Description: 

Write a method called findModSum1.  The method takes a list of integers.  
The method returns the sum of all the elements that are multiples of 3.

Name: findModSum1
Parameters: int[] data
Returns: int

Preconditions: data is a list of integers. 

findModSum1({21,4,6,9,10,12}) → 21 + 6 + 9 + 12 = 48
'''

def findModSum1(data):

	sum = 0

	#loop through each element
	for i in range(0, len(data), 1):

		#check if element is a multiple of 3
		if (data[i] % 3 == 0):
			sum = sum + data[i] #add element if multiple of three


	return sum

a = [21,4,6,9,10,12]
b = []
c = [3]
d = [1,1,1,1,1,1,1,1]
e = [3,6,18]
print(findModSum1(a))










