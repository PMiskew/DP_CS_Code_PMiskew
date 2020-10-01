
def base2ToHex(s):

	HEX = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

	result = ""

	s =  len(s)%4 * "0" + s

	for i in range(0, len(s),4):

		v = s[i: i + 4]
		index = int(v[0])*8 + int(v[1])*4 + int(v[2])*2 + int(v[3])*1
		result = result + HEX[index]

	
	return result

BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

#print(base2ToHex("0010"))
#Simple Test Case
for i in range (0, len(BIN),1):
	print(base2ToHex(BIN[i]))

print(base2ToHex("1011110101"))


