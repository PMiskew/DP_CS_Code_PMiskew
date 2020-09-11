#Mod10Div10 algorithm: Used to access each digit in a number
'''
Theory:

The mod operator (%) will give the remainder when division is performed
14 % 3 = 2

Why?  14/3 = 4R2, mod (%) simpley gives the remainder. 

56%0 = undefined
0%56 = 0

Integer Division is what happens when two integers are divided. When
we integer divide we chop off decimal values. 

In python 3/4 = 0.75, however, in Java (and may other languages) 3/4 = 0. 

Why?  This is becasuse Java see 3 as and an integer and 4 as an integer
and assumes the result should be an integer so it integer divides.  Python
however tries to be helpful and thinks you want the decimals so leaves them

In Python // is integer divid
'''

num = 345
total = 0
while (num > 0):
    total = total + num % 10
    num = num//10

print(total)

'''
num | num > 0 |
345 | 345 > 0 | True RUN LOOP num = 345//10 = 34
34  | 34 > 0  | True RUN LOOP num = 34//10 = 3
3   | 3 > 0   | True RUN LOOP num = 3//10 = 0
0   | 0 > 0   | False EXIT
'''







