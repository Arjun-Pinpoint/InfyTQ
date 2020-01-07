#PF-Assgn-29
def calculate(distance,no_of_passengers):
    cost = 0
    cost = 70 * distance/10
    rest = 0
    rest = no_of_passengers * 80 
    if cost <= rest :
        return abs(cost - rest)
    else :
        return -1

distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
