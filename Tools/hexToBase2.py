
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

def hexToBase2(s):

	if checkDigits(s) == False:
		return -1

	#Parallel Lists
	HEX = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

	result = ""
	for n in range(len(s) - 1, -1, -1):
		for i in range(0, len(HEX),1):
			if (HEX[i] == s[n]):
				result =  BIN[i] + result
				break

	return result



print(hexToBase2("0"))
print(hexToBase2("A12"))
print(hexToBase2("F"))


