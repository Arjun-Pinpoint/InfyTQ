'''
Write a pseudo-code to find out if a given year is a leap year or not.
Any year which is divisible by 4 and not by 100 are leap years. Otherwise,
any year which is divisible by 400 is also a leap year.
'''
input Year
if(Year%4==0 and Year%100!=0) then
display "It is a leap year"
else if(Year%400==0) then
display "It is a leap year"
else
display "It is not a leap year"
end-if
