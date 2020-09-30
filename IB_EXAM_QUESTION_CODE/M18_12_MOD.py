'''

What is changed?

I copied the value into a temp value before processing
Therefore it runs as the solution showins in the exam solution
'''

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
	TEMP = int(getNext()) #ADDED
	if (TEMP > 0):
		ARRAY[X] = TEMP
		COUNTER = COUNTER + 1
		SUM = SUM + ARRAY[X]

print(ARRAY)
print(SUM/COUNTER)