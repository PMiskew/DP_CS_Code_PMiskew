
import math
#input

def findArea():
	#casting to float - changes type
	'''
	x1 = input()
	x1 = float(x1)

	y1 = input()
	y1 = float(y1)

	x2 = input()
	x2 = float(x2)

	y2 = input()
	y2 = float(y2)
	'''
	#Contest Stategy 1 - just set variable values and take inputs after
	x1 = 2
	y1 = 4
	x2 = 4
	y2 = 8


	#process

	#r = ((y2 - y1)**(2) + (x2 - x1)**(2))**(1/2)
	'''
	sqrt is a static/class function contained in the math module. 
	static function does not require an implied object. 

	word = "Emanuel"
	word.upper() #word is the implied object meaning upper is an instance or non-static method
	math.sqrt(7) #math is a modeule containing a bunch of function - no implied object is needed for sqrt
				 #to run.  Therefore we invoke the method with the name of the modele (or nothing). The
				 #method runs purley on the parameters that are passed
	'''
				 
	r = math.sqrt((y2 - y1)**(2) + (x2 - x1)**(2))
	a = 3.14159*r*r
	a = round(a,3)

	print(a)

#Contest Strategy 2 - Write the problem as a function
findArea()

