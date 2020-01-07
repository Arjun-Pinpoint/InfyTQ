'''Write a python function to check whether three given numbers can form the sides of a triangle.
Hint: Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers.
'''
#PF-Assgn-24
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if num1**2+num2**2==num3**2:
        return success
    else:
        return failure

num1=3
num2=3
num3=5
print(form_triangle(num1, num2, num3))
