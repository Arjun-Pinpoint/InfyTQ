'''
Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number.
Also write the pytest test cases to test the program.

Sample Input	Expected Output
12300	12321
12331	12421
'''
#PF-Assgn-46
def nearest_palindrome(number):
    flag=0
    temp=''
    while(flag==0):
        number+=1
        temp=str(number)
        reverse=temp[::-1]
        if(temp==reverse):
            flag=1
    return temp
number=12300
print(nearest_palindrome(number))
