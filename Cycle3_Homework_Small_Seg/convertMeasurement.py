'''
These functions are related to our homework task from the class
where we are exploring the below dwite problem

https://www.nayuki.io/res/dwite-programming-contest-solutions/dwite-200410-p3.pdf

This method helps break down the approach into a smaller part 
which is the conversion of units for comparision

'''


'''
This function takes a float value representing a measurement 
value and a string representing the units.  It returns the 
val in meters

The function returns -1 if the unit is not recognized or
if the value is -1
'''
def findMeters(val, unit):

	if val < 0:
		return -1
	if unit == "mm":
		return val/1000
	elif unit == "cm":
		return val/100
	elif unit == "dm":
		return val/10
	elif unit == "m":
		return val/1

	return -1
print(findMeters(-99,"nm"))


'''
This method converts the passed value from u1 to u2 where
val is a float, u1 and u2 are string values. 
'''
def convertUnits(val,u1,u2,*args):

	factor = ["nm","mm","cm","dm","m"]
	
	#.   10     10     10
	# mm --> cm --> dm --> m
	#
	#Find the index of u1 and u2
	try:
		v1 = factor.index(u1)
		v2 = factor.index(u2)
	except:
		return -1

	print(v1)
	print(v2)
	#Finds the differnece of U1 and U2
	conv = v2 - v1

	return val/(10**conv)
	

try: 
	print(convertUnits(100,"dm","mm","dc"))
except:
	







