'''
Simplier Approach:

Choice of data structure really impacts programming approach.  With the
below approach we used an indexing approach.  If we setup a dictonary 
that uses a key:value pair we can signficantly streamline the algorithm

Second change: Insteand of using a mathematical approach, which still had
some issues we used a counted loop to add 0's to the front of s until it
the length is divisible by 4
'''

def base2ToHexB(s):

	result = ""

	DIC = { "0000":"0",
			"0001":"1",
			"0010":"2",
			"0011":"3",
			"0100":"4",
			"0101":"5",
			"0110":"6",
			"0111":"7",
			"1000":"8",
			"1001":"9",
			"1010":"A",
			"1011":"B",
			"1100":"C",
			"1101":"D",
			"1110":"E",
			"1111":"F"}

	while (len(s)%4 != 0):
		s = "0" + s
	


	for i in range(0, len(s),4):
		v = s[i: i + 4]
		result = result + DIC[v]

	return result

BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
#Simple Test Case
for i in range (0, len(BIN),1):
	print(base2ToHexB(BIN[i]))

print(base2ToHexB("1011110101")) #2 F 5
print(base2ToHexB("1110111110110")) #1 D F 6
#**************************************************
'''
Description:  This function takes a string, representing a binary value.
If s is invalid then the function returns "-1"

Parameter: String s
Return: String

precoditions: -
postconditions: -

'''
def base2ToHexA(s):


	#Declaring a list of strings called HEX and initalizing the elements to all 
	#the HEX characters. HEX is a constant so the variable name is capitalized
	HEX = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	
	#Assignment Statement: Delares result and initalizes it to ""
	#This line stores the resulting Hex value that is returned. 
	result = ""

	
	'''
	1011 1111 
	  B    F

	11 1010 --> 0011 1010 
				 3.    A

	'''
	#This line adds the appropriate amount of zeros to make the length of s divisible
	#by 4
	#Python Specific:  2 * "hi" = "hihi"
	s =  (4 - len(s)%4) * "0" + s #adds 0 to front of string to make len multiple of 4
	'''
	s = "1111"
	s = (4 - 4%4) * "0" + s
	s = 4 * "0" + s
	s = "0000" + s

	#Counted Loop: Looping through s and incrementing by 4

	10111111

	i = 0 [0: 0 + 4] = [0:4] --> "1011"
	i = 4 [4: 4 + 4] = [4:8] --> "1111"
	'''
	for i in range(0, len(s),4):

		#Using substring string to access 4 characters at a time and store
		#the result in v
		v = s[i: i + 4]
		#Accesses each index of v and multiplies it by the corrisponding power of 2
		#to generate base 2 value of the 4 digits
		# 1011 --> 8 + 2 + 1 = 11
		# 1111 --> 8 + 4 + 2 + 1 = 15
		#Casting: We are casting the strings to integer values.  Casting is the process
		#of changing type. 
		index = int(v[0])*8 + int(v[1])*4 + int(v[2])*2 + int(v[3])*1
		#By converting the 4 digit base 2 number into base 10 I can use that as the index
		#in HEX to get the value.
		result = result + HEX[index]

	
	#Resturn result
	return result


#TESTING:
BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

'''
#print(base2ToHex("0010"))
#Simple Test Case
for i in range (0, len(BIN),1):
	print(base2ToHexA(BIN[i]))

print(base2ToHexA("1011110101")) #2 F 5
print(base2ToHexA("1110111110110")) #1 D F 6
'''

