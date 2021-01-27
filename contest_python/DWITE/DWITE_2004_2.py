#Step 1: Take our input. 
time = "00:30"

'''
01234
09:30

'''

#Step 2: break up string
h = time[0:2] # 2 - 0 = 2
h = int(h)

m = time[3:5] # 5 - 3 = 2

timeOfDay = "AM"

if (h >= 12):
	h = h - 12
	timeOfDay = "PM"

if (h == 0):
	h = 12
	
print(str(h)+":"+m+" "+timeOfDay)



