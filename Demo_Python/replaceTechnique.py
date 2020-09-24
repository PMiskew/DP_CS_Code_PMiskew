
'''
If we want to remove a value from a string we can replace it and empty string



'''

s = "j.ohn.smi.th"

s = s.replace(".","") #This collapases the string when removing teh .
print(s)


'''
How does this apply to the question from class:

Description: 

Write a method called findModSum4.  The method takes a list of doubles and returns the sum of the digits. 


Name: findModSum4
Parameters: double[] 
Returns: int

findModSum({1.2,3.14,7.89}) → 1 + 2 + 3 + 1 + 4 + 7 + 8 + 9 = 35 


We have done an example of adding digits, but the problem is that
the values are doubles, decials, 

Covert element to string
replace "." with ""
add remaining digits. 
'''


