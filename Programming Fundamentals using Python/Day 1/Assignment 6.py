'''
Write a pseudo-code to check whether a given number is a palindrome.
Examples of palindrome: 121, 1331, 2332,78900987,123456654321 etc.
'''
input Number
Temp=Number
Reverse=0
while(Number!=0) do
Remainder=Number%10
Reverse=Reverse*10+Remainder
Number=Number/10
end-while
if(Temp==Reverse) then
display "Palindrome"
else
display "Not a Palindrome"
end-if
