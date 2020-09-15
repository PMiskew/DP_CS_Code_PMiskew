'''
Big Ideas:  

Reference Types

'''

'''
Write a function called scaleElementsA that takes an integer value a and 
a list/array reference b.  The function should scale each element of b. 
For example if the list is [1,2,3,4] and the scale factor a = 2. This means
 that the postcondition of the function is that the list/array is set to 
 [2,4,6,8].

Name: scaleElementsA

Parameters: int, int[]


'''
def scaleElementsA(a, b):
    print("Scale Elements A")

    #I Need to loop through every element and multiply it by a
    for i in range(0,len(b),1):
        #if b = [1,2,3,4], i will be 0,1,2,3
        b[i] = a * b[i] #b[i] is said "b at i"

'''
print("START TEST CODE SCALE ELEMENTS A")
l = [1,2,3,4]
print(l)
scaleElementsA(2,l)
print(l)


print("**********************************")
'''

'''
Write a function called scaleElementsB that takes an integer value
a and a list/array reference b.  The function should create a new 
list/array with an equal length of b with each element scaled by a. 
The parameter b should not be changed. For example if the list is 
[1,2,3,4] and the scale factor a = 2. This means that the returned 
array should be [2,4,6,8]. The postcondition of a should be that 
the array is not changed. 

Name: scaleElementsB

Parameters: int, int[]

Return: int[]
'''
def scaleElementsB(a,b):
    print("Scale Elements B")
    
    c = [] #Creates an empty list

    for i in range(0, len(b),1):

        c.append(b[i]*a) #append adds a new element to the list
    
    return c

print("START TEST CODE SCALE ELEMENTS B")
l = [1,2,3,4]
print(l)
result = scaleElementsB(2,l)
print(result)


print("**********************************")


def addStringsSmallLarge(a, b):
    print("Add Strings Small Large")

    
