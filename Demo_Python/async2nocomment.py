def scaleElementsA(a, b):

    for i in range(0,len(b),1):
        b[i] = a * b[i] 

'''
print("TEST CODE scaleElementsA**********************************")
l = [1,2,3,4]
print(l)
scaleElementsA(2,l)
print(l) #printing [2,4,6,8]
print("**********************************")
'''

def scaleElementsB(a,b):

    c = []

    for i in range(0, len(b),1):

        c.append(b[i]*a) #append adds a new element to the list
    
    return c

print("TEST CODE scaleElementsB**********************************")
l = [1,2,3,4]
print(l)
result = scaleElementsB(2,l)
print(l)
print(result)
print("**********************************")














def addStringsSmallLarge(a, b):
    print("Add Strings Small Large")

    result = a + b

    if len(a) > len(b):
        result = b + a
    
    return result

    
