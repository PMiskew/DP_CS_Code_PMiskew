def findSumDICTA(dict):

	sum = 0
	#for each loop - this is a short hand notation for a loop that goes 
	#through every element in a collection sequentially. 
	#WATCH - SO MANY SHORT HAND NOTATIONS IN PYTHON!
	for key in dict:

		if type(dict[key]) == int or type(dict[key]) == float:
			sum = sum + dict[key]
	
	return sum

def findSumDICTB(dict):

	sum = 0

	for key in dict:

		try:
			sum = sum + dict[key]
		except:
			sum = sum
	return sum


dict1 = {"ffdasfeasdf":"cat", "fdassafa":"dog", "fdasdasdf":1, "twrrgre":2, "faea":4}

#Test 2:
#Empty list --> 0
dict2 = {}

#Test 3
#only strings --> 0
dict3 = {"fdasfd":"cat","vbnda":"dog","fdasfdav":"fish"}

#Test 4
#only ints --> 55
dict4 = {"gebaf":1, "fasew":2, "nbv":3, "iuytr":4, "lkjh":5, "qwer":6, "zxcv":7, "poiuyt":8, "jhgf":9, "asdfg":10} 

#***
dictASum = findSumDICTA(dict1)
print("A",dictASum)

dictBSum = findSumDICTB(dict1)
print("B",dictASum,"\n")

#***
dictBSum = findSumDICTA(dict2)
print("B",dictBSum)

dictBSum = findSumDICTB(dict2)
print("B",dictBSum,"\n")

#***
dictCSum = findSumDICTA(dict3)
print("C",dictCSum)

dictCSum = findSumDICTB(dict3)
print("B",dictCSum,"\n")

#***
dictDSum = findSumDICTA(dict4)
print("D",dictDSum)

dictDSum = findSumDICTB(dict4)
print("B",dictDSum,"\n")

















