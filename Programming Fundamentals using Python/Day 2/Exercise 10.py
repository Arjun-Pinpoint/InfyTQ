'''
Write a program to take the turtle to its destination - north, south, east or west based on the destination it wants to reach. Refer the output screens provided for each destination.
'''
import turtle 
wn = turtle.Screen()        
wn.setup(540,508)           
alex = turtle.Turtle()      
alex.shape("turtle")        
alex.color("blue")              
destination="north"
if destination=="south":
alex.right(90)
alex.forward(50)
elif destination=="east":
alex.forward(50)
elif destination=="north":
alex.left(90)
alex.forward(50)
elif destination=="west":
alex.left(180)
alex.forward(50)
else:
alex.write("      look like you have a wrong distination")
