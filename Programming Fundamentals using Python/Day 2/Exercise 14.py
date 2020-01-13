'''
A teacher in a school wants to find and display the grade of a student based on his/her percentage score. The criterion for grades is as given below:
Score (both inclusive)	Grade
Between 80 and 100	A
Between 73 and 79	B
Between 65 and 72	C
Between 0 and 64	D
Any other value	Z
Assume that the percentage score is a whole number.

Write a python program for the above requirement. Identify the test data and use it to test the program.
SOLUTION:
'''
n=int(input())
if n<100 and n>80:
    print("A")
elif n<79 and n>73:
    print("B")
elif n<72 and n>65:
    print("C")
elif n<65 and n>0:
    print("D")
else:
    print("Z")
