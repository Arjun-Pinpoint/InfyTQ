def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0 
    total_ticket_cost=no_of_adults*(37550)+no_of_children*(1/3*37550)
    return total_ticket_cost
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)
