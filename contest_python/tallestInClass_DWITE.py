'''
Recommendation:

This problem can be daunting, however, if you break it apart to some components and tackle those
it falls apart nicely. 

1. 	Start by managing the input. Assuming you store the data as a list of strings, create three 
	new lists and copy in the data.  The first two elements in this parallel list structure look
	as follows

				name = ["Jim","Sally",. . .]
				height = [1.45, 187, . . . ]
				units = ["m", "cm", . . .]

	HL - You could copy it into a 2D list 

	data2D = [	["Jim","Sally",. . .],
				[1.45, 187, . . . ],
				["m", "cm", . . .],
			]
]

2. 	Start off by simplifying the problem by assuming
		a) All measurements are in the same unit
		b) You only want to find the single tallest. 

2.  Create a function that coverts any unit to meters.  What it converts it to doesn't matter, but
	this allows you to send any meansurment through it and get a standard measurement that can be 
	compared. 

'''

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
