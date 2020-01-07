'''
The program provided in the starter code tab is written to display “*” as per the expected output given below. But the code is having logical errors, debug the program using Eclipse Debugger and correct it.
Expected Output:
*****
****
***
**
*
'''
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("")
