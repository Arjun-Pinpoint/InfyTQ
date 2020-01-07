'''
Write a pseudo-code to find the sum of numbers divisible by 4.The pseudo-code must allow the user to accept a number and add it to the sum if it is divisible by 4. It should continue accepting numbers as long as the user wants to provide an input and should display the final sum.
'''
Sum=0
Choice='Yes'
while(Choice=='Yes') do
input Number
if(Number%4==0) then
Sum=Sum+Number
end-if
display "Do you want to continue? (Enter Yes or No)"
input Choice
end-while
display Sum
