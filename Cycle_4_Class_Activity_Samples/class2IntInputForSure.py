'''
print("Dog Age Calculator")

#Setting an infinite loop that can only exit with the break statements
#The break staetment is only reached if we can cast age to an int
while (True):
	
	try:
		age = input("What is your age: ")
		age = int(age)
		break #breaks out of the loop
	except:
		print("Please input an integer number")

dogAge = age*7

#print("Your are"+str(dogAge)+"years old.")

print("Your are",dogAge,"years old.")

print("Cat Age Calculator")
'''
#Setting an infinite loop that can only exit with the break statements
#The break staetment is only reached if we can cast age to an int
while (True):
	
	
	age = input("What is your age: ")
	
	if age.isnumeric():

		catAge = int(age)*6
		break
	else:
		print("Please input an integer number")

#print("Your are"+str(dogAge)+"years old.")

print("Your are",catAge,"years old.")







