


DATA = open("DATA.txt","r")

def getNext():

	VAL = DATA.readline()
	VAL = VAL.strip()
	return VAL



	print(getNext())


# IB assumes indexes exist so I created an empty array
# with seven elements.  I woudl have liked to see this 
# in the question for clarity. 



ARRAY = [0,0,0,0,0,0,0]
COUNTER = 0
SUM = 0

for X in range(0, 7, 1):

	if (int(getNext()) > 0):
		ARRAY[X] = int(getNext())
		COUNTER = COUNTER + 1
		SUM = SUM + ARRAY[X]

print(ARRAY)
print(SUM/COUNTER)