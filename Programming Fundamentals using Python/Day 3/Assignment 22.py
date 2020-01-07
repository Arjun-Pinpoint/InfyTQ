'''
Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.
Also write the pytest test cases to test the program.
'''
#PF-Assgn-22
def find_leap_years(given_year):
    list_of_leap_years=[]
    count=0
    while(count<15):
        if(given_year%400==0 or given_year%4==0):
            list_of_leap_years.append(given_year)
            count+=1
        given_year+=1
    
    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
