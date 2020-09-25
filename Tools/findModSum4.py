'''
Description: 

Write a method called findModSum4.  The method takes a list of doubles and 
returns the sum of the digits. 


Name: findModSum4
Parameters: double[] data
Returns: int

findModSum4({1.2,3.14,7.89}) → 1 + 2 + 3 + 1 + 4 + 7 + 8 + 9 = 35 

'''

def findModSum4(data):

	sum = 0
	#First loop will loop through the elements of data
	for i in range(0, len(data),1):

		a = data[i]
		a = str(a) #casts a to string 
		a = a.replace(".","")

		for j in range(0, len(a),1):

			v = a[j]
			v = int(v) #casts v to an integer
			sum = sum + v

	return sum

a = [1.2,3.14,7.89]
print(findModSum4(a))






