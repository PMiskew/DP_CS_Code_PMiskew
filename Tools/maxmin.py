l = [100,2,3]
#abstraction: this is the process of hiding how something is done. 
print(max(l))

'''
WATCH: 
'''
def findMaxConcern(a):

    #In the below a is called the IMPLIED OBJECT - If a list invokes
    #a function as an implied object is changes the list.
    a.sort() #If I sort the list from lowest to highest
    return a[len(a) - 1]


#CAUTION:   Don't call variable max it can cause
#           problems since function is called max
l = [100,2,3]
w = l #give w and l the same refernce. 
z = l.copy()

print("L = ",l)
m = findMaxConcern(l)
print(m)
print(l)

print("W =",w)
'''
findMax takes list of integers and returns max value.
The list a must contain at least 1 element and a must
remain unchanged when the function is done. 
'''
def findMax(a):

    #Big Idea: Set the correct value to an element in the list
    m = a[0]
    for i in range(0,len(a),1):
        m = max(m,a[i]) #max is OVERLOADED method

    return m

l = [100,2,3]
m = findMax(l)
print(m)
print(l) #l not changed


