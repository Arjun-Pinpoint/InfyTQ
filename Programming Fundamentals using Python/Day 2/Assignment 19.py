'''
FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.
A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate. Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than the vegetarian combo.Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point. The delivery charges are as mentioned below:
Distance in kms	Delivery charge in Rs per km
For first 3kms	0
For next 3kms	3
For the remaining	6
Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery point, write a python program to calculate the final bill amount to be paid by a customer.

The below information must be used to check the validity of the data provided by the customer: 
•	Type of food must be ‘V’ for vegetarian and ‘N’ for non-vegetarian.
•	Distance in kms must be greater than 0.
•	Quantity ordered should be minimum 1.
If any of the input is invalid, the bill amount should be considered as -1.


Solution: 
'''
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    if quantity_ordered>=1 and distance_in_kms>0:
        deli_cost = 0
        bill_amount=0
        dist = [(3,0),(6,3),(7,6)]
        if food_type == 'V':
            food_cost = quantity_ordered * 120
        elif food_type == 'N':
            food_cost = quantity_ordered * 150
        else:
            return -1
        dist_covered = 0
        while dist_covered<= distance_in_kms:
            for distance in dist:
                if dist_covered<= distance[0]:
                    value = distance[1]
                    break
            deli_cost = deli_cost + value
            dist_covered=dist_covered+1
            bill_amount = food_cost + deli_cost
        return bill_amount
    else:
        return -1
bill_amount=calculate_bill_amount("N",2,7)
