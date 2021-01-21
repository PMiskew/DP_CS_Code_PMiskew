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

	if unit < 0:
		return -1
	if units == "mm":
		return val/1000
	elif units == "cm":
		return val/100
	elif units == "dm":
		return val/10
	elif units == "m":
		return val/1


	return -1


def convertUnits(val,u1,u2):


	factor = ["mm","cm","dm","m"]
	v1 = factor.index(u1)
	v2 = factor.index(u2)

	conv = v2 - v1

	if conv < 0:
		return abs(val*(conv*10))

	return val/(conv*10)
	


print(convertUnits(100,"mm","cm"))








