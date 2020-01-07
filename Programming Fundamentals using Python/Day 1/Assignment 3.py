'''
Jack and his three friends have decided to go for a trip by sharing the expenses of the fuel equally.
Write a Python program to calculate the amount (in Rs) each of them need to put in for the complete (both to and fro) journey.
The program should also display True, if the amount to be paid by each person is divisible by 5, otherwise it should display False. (Hint: Use the relational operators in print statement.)
Assume that mileage of the vehicle, amount per litre of fuel and distance for one way are given.
Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

Sample Input	Expected Output
Mileage of the vehicle (km/litre of fuel)	Amount per litre of fuel (Rs)	Distance for one way (kms)	
12	65	96	260.0
True
12	40	190	
'''
import math
mileage=12
amount_per_litre=72
distance_one_way=102
per_head_cost=0
divisible_by_five=False
per_head_cost=per_head_cost*2*distance_one_way/(mileage*4)
divisible_by_five=(per_head_cost*2*distance_one_way/(mileage*20)==math.floor(per_head_cost*2*distance_one_way/(mileage*20)))

print(per_head_cost, divisible_by_five)
