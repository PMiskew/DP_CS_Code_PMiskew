
'''
Simplier Approach: Dictionaries
'''

def hexToBase2_B(s):
	result = ""

	DIC = { "0":"0000",
			"1":"0001",
			"2":"0010",
			"3":"0011",
			"4":"0100",
			"5":"0101",
			"6":"0110",
			"7":"0111",
			"8":"1000",
			"9":"1001",
			"A":"1010",
			"B":"1011",
			"C":"1100",
			"D":"1101",
			"E":"1110",
			"F":"1111"}

	
	for i in range(0, len(s), 1):
		result = result + DIC[s[i]]

	return result


print(hexToBase2_B("0"))
print(hexToBase2_B("A12"))
print(hexToBase2_B("F"))
'''
  S = passed string parameter only containing hex characters
  HEX = ["0","1","2", . . .,"E",F"]
  BIN = ["0000","0001","0010",....,"1110","1111"]	

  RESULT = ""
  
  Loop N from S.length - 1 to 0:
  	Loop I from 0 to len(HEX) - 1:
  		if HEX[I] == S[N]
  			RESULT = BIN[I] + RESULT
		end if
	end loop
  end loop

  return RESULT



'''
def checkDigits(s):
	print("CHECKING")
	return True


'''
Description: This function takes a single hexadecimal character and returns
the 4 digit binary representation

Parameters: String h
Return: String
'''
def hexToBase2(h):

	HEX = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
	for i in range(0, len(HEX),1):
			if (HEX[i] == s[n]):
				return BIN[i]

	return -1

'''
Description: This function returns true if s contains only hexadecimal values
Parameter: String s
Return: Boolean
'''
def checkDigits(s):

	org = len(s)

	s = s.replace("0","")
	s = s.replace("1","")
	s = s.replace("2","")
	s = s.replace("3","")
	s = s.replace("4","")
	s = s.replace("5","")
	s = s.replace("6","")
	s = s.replace("7","")
	s = s.replace("8","")
	s = s.replace("9","")
	s = s.replace("A","")
	s = s.replace("B","")
	s = s.replace("C","")
	s = s.replace("D","")
	s = s.replace("E","")
	s = s.replace("F","")
	
	#Returns false
	return len(s) == 0




'''
Description: This function takes a string containing HEX characters
and returns the base 2 conversation of the argument as a string

Parameters: String s
Return String 
precondition: S contains only hex characters

'''
def hexToBase2_A(s):

	if checkDigits(s) == False:
		return -1

	#Parallel Lists
	HEX = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

	result = ""
	#Loop through s in reverse
	for n in range(len(s) - 1, -1, -1):
		for i in range(0, len(HEX),1):
			if (HEX[i] == s[n]):
				result =  BIN[i] + result
				break

	return result

print(hexToBase2_A("0"))
print(hexToBase2_A("A12"))
print(hexToBase2_A("F"))


