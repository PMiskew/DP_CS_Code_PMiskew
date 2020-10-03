
def base10ToBase2(n):

	result = ""

	while n > 0:

		result = str(n % 2) + result
		n = n//2

	return result

print(base10ToBase2(53))
print(base10ToBase2(62))
print(base10ToBase2(45))


'''
53 = 110101

1   1 --> 1 - 1 = 0
2   0 
4   1 --> 5 - 4 = 1
8   0
16  1 --> 21 - 16 = 5
32  1 --> 53 - 32 = 21

53 / 2 = 26 R 1

26 / 2 = 13 R 0

13 / 2 =  6 R 1

 6 / 2 =  3 R 0

 3 / 2 =  1 R 1 

 1 / 2 =  0 R 1

53 = 110101


Base 10 To Base 3

With base 3 we have three valid digits 0,1,2

53 = 

53 / 3 = 17 R 2

17 / 3 = 5 R 2

 5 / 3 = 1 R 2

 1 / 3 = 0 R 1

53 = 1222

341 = 3 * 100 + 4 * 10 + 1 * 1
    = 3 * 10^2 + 4*10^1 + 1*10^0


53 = 1 * 3^3 + 2*3^2 + 2*3^1 + 2*3^0
   = 1 * 27 + 2 * 9 + 2 * 3 + 2 * 1
   = 27 + 18 + 6 + 2
   = 53
'''

def base10ToBaseB(n, b):

	result = ""

	while n > 0:

		result = str(n % b) + result
		n = n//b

	return result


print(base10ToBaseB(53,3))



















