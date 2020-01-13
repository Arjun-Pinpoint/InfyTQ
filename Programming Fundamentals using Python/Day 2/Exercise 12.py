'''
Write a Python program to find and display the maximum of three given numbers.

Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:
Sample Input	Expected Output
Num1	Num2	Num3	
1	2	3	3
3	4	1	

SOLUTION:
'''
def working(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>c:
        print(b)
    else:
        print(c)
a=input()
b=input()
c=input()
working(a,b,c)
