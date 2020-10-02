'''
Description: 

Write a method called findModSum2.  The method takes a list of integers and 
two integer values.  The method returns the sum of all the elements that 
are between a (exclusive) and b (exclusive). 

Name: findModSum2
Parameters: int[] data, int a, int b
Returns: int

Preconditions: data is a list of integers a and b are both integers. 

findModSum2({2,3,10,9,14,25,3,100},5,25} → 10 + 9 + 14 = 33


'''
def findModSum2(data, a, b):

	sum = 0

	large = max(a,b)
	small = min(a,b)

	for i in range(0, len(data), 1):

		if (data[i] > small and data[i] < large):
			sum = sum + data[i]

	return sum


a = [2,3,10,9,14,25,3,100]
print(findModSum2(a,25,5))
























