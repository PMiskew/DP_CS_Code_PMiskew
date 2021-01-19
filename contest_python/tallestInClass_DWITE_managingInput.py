
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

		loc = data[i].index(' ')
		n = data[i][0:loc]
		name.append(n)
		
		loc1 = data[i].index(' ',loc+1)
		
		h = data[i][loc + 1:loc1]
		height.append(float(h))

		u = data[i][loc1+1:]
		units.append(u)


	print(name)
	print(height)
	print(units)


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


			try:
				loc = val.index(" ")
				data1.append(val[0:loc])
				val = val[loc+1:]
			except:
				data1.append(val)
				break
		
	print(data1)

approach2()
