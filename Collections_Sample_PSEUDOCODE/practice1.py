'''
Given a collection of integers C find the sum of all the odd integers and output
the value

* 	Collection is a collection of data it is a general term for a data structure
* 	Lists, arrays, stacks, queues are collections
* 	You cannot calculate the length of a collection. 
* 	I can't use a counted loop to go through a collection because I don't know 
	how long it is
*	With a list or a array you can access any element using the index. 
*	With a collection you must "travel" to the value
	*By travel we mean use the .getNext() function

                  X
C = [1,3,56,3,4,6,3]

print(C.hasNext()) //print True
print(C.getNext()) // print 1
print(C.hasNext()) //print True
print(C.getNext()) // print 3
print(C.hasNext()) //print True
print(C.getNext()) // print 56
print(C.hasNext()) //print True
print(C.getNext()) // print 3
print(C.hasNext()) //print True
print(C.getNext()) // print 4
print(C.hasNext()) //print True
print(C.getNext()) // print 6
print(C.hasNext()) //print True
print(C.getNext()) // print 3
print(C.hasNext()) // print False
print(C.getNext()) // ERROR there is no next - CRASH!!!

*There is no way to jump around.  

Starting Fresh

print(C.getNext()) // print 1
print(C.getNext()) // print 3
print(C.getNext()) // print 56
C.resetNext() //returns the next value to the start. 
print(C.getNext()) // print 1


We have a stand loop strucutre to go through a list

list/array has a length that I can calculate and indexs which are 0 to length - 1
        0 1 2 3 4 5 6 
list = [1,3,4,5,3,5,7]

print out values

JS - 

for (i = 0; i < list.length; i = i + 1) {
	console.log(list[i])
}

Python - 

for i in range(0, len(list), 1):
	print(list[i])



Trace Table

i   | i < len(list) |
0	| 0 < 7 TRUE	 | RUN LOOP
1	| 1 < 7 TRUE	 | RUN LOOP
2	| 2 < 7 TRUE	 | RUN LOOP
3	| 3 < 7 TRUE	 | RUN LOOP
4	| 4 < 7 TRUE	 | RUN LOOP
5	| 5 < 7 TRUE	 | RUN LOOP
6	| 6 < 7 TRUE	 | RUN LOOP
7	| 7 < 7 FALSE	 | EXIT LOOP

We have looped through every index meaning I can acces each element


LOOK AT THIS QUESTION: Just like the collection question, but it specifies
a list

Given a list of integers LIST find the sum of all the odd integers and output
the value


SUM = 0

for i in range(0, len(LIST), 1):
	if (LIST[i] % 2 == 1):
		SUM = SUM + LIST[I]
output sum



WHAT DOES THIS MEAN FOR COLLECTIONS!!
Given a collection of integers C find the sum of all the odd integers and output
the value


SUM = 0

loop while (C.hasNext()):
	NUM = C.getNext()
	if (NUM % 2 == 1) then
		SUM = SUM + NUM
	end if
end loop

list = [1,3,4,5,3,5,7]

C.hasNext() | NUM. | NUM % 2 == 1  | SUM
   XXX		| XXX  | XXX		   |  0
   True     | 1    |  1 % 2 == 1 T | 0 + 1
   TRUE.    | 3.   |  3 % 2 == 1 T.| 1 + 3 = 4
   TRUE.    |.4    |. 4 % 2 == 1 F.| 
   TRUE.    | 5.   |  5 % 2 == 1 T | 4 + 5 = 9
   TRUE.    | 3.   |  3 % 2 == 1 T.| 9 + 3 = 12
   TRUE.    | 5.   |  5 % 2 == 1 T | 12 + 5 = 17
   TRUE.    | 7.   |  7 % 2 == 1 T.| 17 + 7 = 24
   FALSE EXIT LOOPS 

    




'''