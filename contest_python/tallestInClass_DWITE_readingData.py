
'''


'''
def approach1():

	#holds a reference to the file TALLEST.txt and is prepared to
	#write to it. 

	file = open("TALLEST.txt","r")
	
	#creates an empty list
	data = []

	#Short hand loop structure which is essential
	#while file.hasNext()
	#This is a FOR EACH loop
	for lines in file:

		#This will take 1 line of text in the list
		#will create a new list by separating on spaces.
		temp = lines.replace("\n","").split(" ")

		#append it to data
		data.append(temp)

	print(data)


#approach1()

def approach2():

	file = open("TALLEST.txt","r")

	lines = int(file.readline())

	data = []

	for i in range(0, 12, 1):

		temp = file.readline().replace("\n","").split(" ")
		data.append(temp)
		
	
	print(data)



#approach2()


def approach3():

	file = open("TALLEST.txt","r")

	lines = int(file.readline())

	name = []
	height = []
	unit = []

	for i in range(0, lines, 1):

		temp = file.readline().replace("\n","").split(" ")
	
		name.append(temp[0])
		height.append(temp[1])
		unit.append(temp[2])

	print(name)
	print(height)
	print(unit)



