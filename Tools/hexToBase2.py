
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

	s = s.reaplaceAll("0","")
	s = s.reaplaceAll("1","")
	s = s.reaplaceAll("2","")
	s = s.reaplaceAll("3","")
	s = s.reaplaceAll("4","")
	s = s.reaplaceAll("5","")
	s = s.reaplaceAll("6","")
	s = s.reaplaceAll("7","")
	s = s.reaplaceAll("8","")
	s = s.reaplaceAll("9","")
	s = s.reaplaceAll("A","")
	s = s.reaplaceAll("B","")
	s = s.reaplaceAll("C","")
	s = s.reaplaceAll("D","")
	s = s.reaplaceAll("E","")
	s = s.reaplaceAll("F","")

	#Returns false
	return len(s) == org




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


