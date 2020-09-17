l = [100,2,3]
print(max(l))

def findMaxConcern(a):

    a.sort()
    return a[len(a) - 1]


#CAUTION:   Don't call variable max it can cause
#           problems since function is called max
l = [100,2,3]
m = findMaxConcern(l)
print(m)
print(l) #notice l is changed

'''
findMax takes list of integers and returns max value
the list must contain at least 1 element and a must
remain unchanged
'''
def findMax(a):

    m = a[0]
    for i in range(0,len(a),1):
        m = max(m,a[i]) #max is OVERLOADED method

    return m

l = [100,2,3]
m = findMax(l)
print(m)
print(l) #l not changed


