
file = open("DATA1.txt","r")

#This will read the whole data in one go
'''
content = file.read()
print(content)
'''

#This will read one line at a time
for aline in file:
	print(aline)