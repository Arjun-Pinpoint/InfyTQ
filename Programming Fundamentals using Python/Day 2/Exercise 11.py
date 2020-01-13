'''
Write a python program that displays a message as follows for a given number:
a.	If it is a multiple of three, display "Zip".
b.	If it is a multiple of five, display "Zap".
c.	If it is a multiple of both three and five, display "Zoom".
d.	If it does not satisfy any of the above given conditions, display "Invalid".

Solution: 
'''
def display(num):
    message=""
    if num%3==0 and num%5==0:
        message="zoom"
    elif num%3==0:
        message="zip"
    elif num%5==0:
        message="zap"
    else:
        message="invalid"
    return message
message=display(15)
print(message)
