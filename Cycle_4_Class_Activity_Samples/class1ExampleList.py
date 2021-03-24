
#APPROACH 1: Using the type function to check type
def findSumLSTA(lst):

	sum = 0
	for i in range(0, len(lst), 1):

		if type(lst[i]) == int or type(lst[i]) == float:
			sum = sum + lst[i]


	return sum

#Approach 2: Using the try except Structure you can achieve the same result by managing the error
def findSumLSTB(lst):

	sum = 0
	for i in range(0, len(lst), 1):

		try:
			sum = sum + lst[i]
		except:
			sum = sum #No change - you need a line in here with the except - Is there 


	return sum


#Test Code findSumLSTA
#Sample lists for testing

#Test 1:
#No floats, No numeric values hiding as strings --> 7
lst1 = ["cat","dog",1,2,4]

#Test 2:
#Empty list --> 0
lst2 = []

#Test 3
#only strings --> 0
lst3 = ["cat","dog","fish"]

#Test 4
#only ints --> 55
lst4 = [1,2,3,4,5,6,7,8,9,10] 

#QUESTION: 	What test cases did I miss?
#QUESTION:  How does the putput change when one of the numbers is a decimal?  Try it on 
#			on one of the lst. 


#NOTE: Using short hand notation to avoid casting
#***
lstA1Sum = findSumLSTA(lst1)
print("A",lstA1Sum)

lstB1Sum = findSumLSTB(lst1)
print("B",lstB1Sum,"\n")

#***
lstA2Sum = findSumLSTA(lst2)
print("A",lstA2Sum)

lstB2Sum = findSumLSTA(lst2)
print("B",lstB2Sum,"\n")

#***
lstA3Sum = findSumLSTA(lst3)
print("A",lstA3Sum)

lstB3Sum = findSumLSTA(lst3)
print("B",lstB3Sum,"\n")


#***
lstA4Sum = findSumLSTA(lst4)
print("A",lstA4Sum)


lstB4Sum = findSumLSTB(lst4)
print("B",lstB4Sum,"\n")