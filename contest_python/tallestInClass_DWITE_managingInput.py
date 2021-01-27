#There are two approaches shown here. Each sets up things differently for the problem

def approach4():

	data = ["Jim 1.45 m",
		"Sally 187 cm",
		"Joey 1064 mm",
		"Roel 15.23 dm",
		"Karl 134 cm",
		"Melanie 18.9 dm",
		"Jill 1.54 m",
		"Sam 133 cm",
		"Joel 1877 mm",
		"Roger 17.83 dm",
		"Karen 178 cm",
		"Marnie 17.9 dm"]

	name = []
	height = []
	units = []

	for i in range(0, len(data), 1):

		temp = data[i].split(" ")
		name.append(temp[0])
		height.append(temp[1])
		units.append(temp[2])

approach0()
#With approach 1 we rely on the OVERLOADED nature of indx function and the fact that 
#we know every elemetn in data has 2 spaces.  
def approach1():

	data = ["Jim 1.45 m",
			"Sally 187 cm",
			"Joey 1064 mm",
			"Roel 15.23 dm",
			"Karl 134 cm",
			"Melanie 18.9 dm",
			"Jill 1.54 m",
			"Sam 133 cm",
			"Joel 1877 mm",
			"Roger 17.83 dm",
			"Karen 178 cm",
			"Marnie 17.9 dm"]

	name = []
	height = []
	units = []

	for i in range(0,len(data),1):

		'''
		index returns the first instance of a passed string

		val = "Jim 1.45 m"
		val.index(' ') --> 3
		'''
		loc = data[i].index(' ')
		n = data[i][0:loc]
		name.append(n)
		
		'''
		looks similary but index takes 2 parameters
		index is an OVERLOADED method
		'''
		loc1 = data[i].index(' ',loc+1)
		
		h = data[i][loc + 1:loc1]
		height.append(float(h))

		'''
		pull out units
		'''
		u = data[i][loc1+1:]
		units.append(u)


	print(name)
	print(height)
	print(units)


'''
In approach 1 we know that there is always 2 spaces, but
what if there is an unknown number of spaces
'''
def approach2():

	data = ["Jim 1.45 m",
	"Sally 187 cm",
	"Joey 1064 mm",
	"Roel 15.23 dm",
	"Karl 134 cm",
	"Melanie 18.9 dm",
	"Jill 1.54 m",
	"Sam 133 cm",
	"Joel 1877 mm",
	"Roger 17.83 dm",
	"Karen 178 cm",
	"Marnie 17.9 dm"]

	data1 = []

	for i in range(0,len(data),1):

		'''
		Java People:  In Java this is a lot cleaner since the indexOf method returns a -1 
		if the value is not located.  Therefore we just say while loc != -1.  However, python
		throws an error so we use this try except function. 
		'''

		val = data[i]
		while True:
'''
			val = "Jim 1.45 m"
			loc = 3
			val = "1.45 m"
			loc = 4
			val = "m"
			loc = THIS CAUSES AN ERROR AND CRASH!

			try except strucutures allow you do override the
			default crash process. 

'''
			try:
				loc = val.index(" ")
				data1.append(val[0:loc])
				val = val[loc+1:]
			except:
				#This gets executed when the program crashes
				data1.append(val)
				break
		
	print(data1)

#Approach 3 creates a 2D array structure where each row represents one person
'''
A 2D list/array is simply adn array of arrays

data = [	["Jim",1.45, "m"],
			["Sally",187,"cm"],
			.
			.
			.
			["Marnie",[17.9],["dm"]
		]

'''
def approach3():

	data = ["Jim 1.45 m",
			"Sally 187 cm",
			"Joey 1064 mm",
			"Roel 15.23 dm",
			"Karl 134 cm",
			"Melanie 18.9 dm",
			"Jill 1.54 m",
			"Sam 133 cm",
			"Joel 1877 mm",
			"Roger 17.83 dm",
			"Karen 178 cm",
			"Marnie 17.9 dm"]

	data1 = []

	for i in range(0, len(data), 1):


		val = data[i]
		while True:

			temp = []
			try:
				loc = val.index(" ")
				temp.append(val[0:loc])
				val = val[loc+1:]
			except:
				temp.append(val)
				break

			data1.append(temp)

	print(data1)

