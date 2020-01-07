'''
A three digit number is said to be an “Armstrong number” if the sum 
the third power of its individual digits is equal to the number itself.
Example: 371 is an Armstrong number as 371 = 33 + 73 + 13
407 is an Armstrong number as 407 = 43 + 03 + 73
Write a pseudo-code to check whether a given three digit number is an
Armstrong number.
'''
input Number
Temp=Number
Sum=0
while(Number!=0) do
Remainder=Number%10
Sum=Sum+Remainder*Remainder*Remainder
Number=Number/10
end-while
if(Temp==Sum) then
display "This is an Armstrong Number"
else
display "This is not an Armstrong Number"
end-if
