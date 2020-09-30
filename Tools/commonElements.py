'''
This method takes two lists and returns a new list containing
the common elements from both lists.
'''
def commonElements(l1,l2):

	l3 = []

	for i in range(0, len(l1),1):

		for j in range(0, len(l2),1):

			if l1[i] == l2[j]:
				l3.append(l1[i])

	return l3


#Trace Table
'''
l1 = ["monkey","cat","moose"]
l2 = ["cat","dog","fish","monkey","cat"]

 i | i < 3 | j  | j < 5 | l1[i] == l2[j]               | l3
 0 | TRUE  | 0  | TRUE  | "monkey" == "cat"      FALSE | 
   |       | 1  | TRUE  | "monkey" == "dog"      FALSE |
   |       | 2  | TRUE  | "monkey" == "fish"     FALSE |
   |       | 3  | TRUE  | "monkey" == "monkey"   TRUE  | ["monkey"]
   |       | 4  | TRUE  | "monkey" == "cat"      FALSE |
   |       | 5  | FALSE |                              |
 1 | TRUE  | 0  | TRUE  | "cat" == "cat"         TRUE  | ["monkey","cat"]
   |       | 1  | TRUE  | "cat" == "dog"         FALSE |
   |       | 2  | TRUE  | "cat" == "fish"        FALSE |
   |       | 3  | TRUE  | "cat" == "monkey"      FALSE |
   |       | 4  | TRUE  | "cat" == "cat"         TRUE  | ["monkey","cat","cat"]
   |       | 5  | FALSE |                              |
 2 | TRUE  | 0  | TRUE  | "moose" == "cat"       FALSE | 
   |       | 1  | TRUE  | "moose" == "dog"       FALSE |
   |       | 2  | TRUE  | "moose" == "fish"      FALSE |
   |       | 3  | TRUE  | "moose" == "monkey"    FALSE |
   | 	   | 4  | TRUE  | "moose" == "cat"       FALSE |
 3 | FALSE | EXIT LOOP

l1 = ["cat","dog","fish","monkey","cat"]
l2 = ["monkey","cat","moose"]

i  | i < 5 | j | j < 3 | l1[i] == l2[j]                | l3
0  | TRUE. | 0 | TRUE  | "cat" == "monkey" 		 FALSE |  
   |       | 1 | TRUE  | "cat" == "cat"          TRUE  | ["cat"]
   |       | 2 | TRUE  | "cat" == "moose"        FALSE |
   |       | 3 | FALSE |                               |
1  | TRUE  | 0 | TRUE  | "dog" == "monkey"       FALSE |
   |       | 1 | TRUE  | "dog" == "cat"          FALSE |
   |       | 2 | TRUE  | "dog" == "moose"        FALSE |
   |       | 3 | FALSE |                               |
2  | TRUE  | 0 | TRUE  | "fish" == "monkey"      FALSE |
   |       | 1 | TRUE  | "fish" == "cat"         FALSE |
   |       | 2 | TRUE  | "fish" == "moose"       FALSE |
   |       | 3 | FALSE | 
3  | TRUE  | 0 | TRUE  | "monkey" == "monkey"    TRUE  | ["cat","monkey"]
   |       | 1 | TRUE  | "monkey" == "cat"       FALSE |
   |       | 2 | TRUE  | "monkey" == "moose"     FALSE |
   |       | 3 | FALSE | 
4  | TRUE  | 0 | TRUE  | "cat" == "monkey"       FALSE |
   |       | 1 | TRUE  | "cat" == "cat"          TRUE  | ["cat","monkey","cat"]
   |       | 2 | TRUE  | "cat" == "moose"        FALSE |
   |       | 3 | FALSE | 

'''

def commonElementB(l1,l2):

	#What is the post condition you have to discuss here?
	l1.sort()
	l2.sort()

	for i in range(0, len(l1),1):

		for j in range(0, len(l2),1):

			if l1[i] == l2[j]:
				l3.append(l1[i])
			if l1[i] > l2[j]:
				return l3

	return l3



#Notice how 
lst1 = ["cat","dog","fish","monkey","cat"]
lst2 = ["monkey","cat","moose"]

#Test Case 1: Common Elements - testing swapping parameters
#There is a problem here. 
lstA = commonElements(lst1,lst2) # ["monkey","cat"]
print(lstA)
lstA = commonElements(lst2,lst1) # ["monkey","cat"]
print(lstA)


#Test Case 2: Empty List
lst3 = []
lstB = commonElements(lst1,lst3) # []
print(lstB)



#Test Case 4: No common elements
lst3 = ["hockey","swimming"]
lst1 = ["cat","dog","fish","monkey","cat"]






