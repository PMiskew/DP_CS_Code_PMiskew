def convertUnits(val,u1,u2):

	factor = ["nm","mm","cm","dm","m"]
	
	try:
		v1 = factor.index(u1)
		v2 = factor.index(u2)
	except:
		return -1

	
	conv = v2 - v1

	return val/(10**conv)


file = open("DATA1.txt","r")

lines = int(file.readline())

data = []

for i in range(0, 12, 1):

	temp = file.readline().replace("\n","").split(" ")
	data.append(temp)

#Convert all measurements to meters
for i in range(0,len(data),1):

	data[i][1] = convertUnits(float(data[i][1]),data[i][2],"m")

#stores 
tallest = []


#Find max five times, but each time settings 
#a new upper limit
for i in range(0, len(data),1):
 





print(data)


