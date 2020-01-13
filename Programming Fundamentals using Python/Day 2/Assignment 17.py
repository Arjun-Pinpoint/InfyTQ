'''
An organization has decided to provide salary hike to its employees based on their job level. Employees can be in job levels 3, 4 or 5.
Hike percentage based on job levels are given below:
Job level	Hike Percentage (applicable on current salary)
3	15
4	7
5	5
In case of invalid job level, consider hike percentage to be 0.
Given the current salary and job level, write a python program to find and display the new salary of an employee. Identify the test data and use it to test the program.
Solution:
'''
def find_new_salary(current_salary,job_level):
    hike = [(3,15),(4,7),(5,5)]
    for i in hike:
        if job_level in i:
            new_salary = (current_salary * (100+i[1]))//100
            return new_salary
        else:
            return current_salary
new_salary=find_new_salary(15000,3)
print(new_salary)
