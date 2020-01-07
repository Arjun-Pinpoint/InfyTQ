'''
Write a program to create a following pattern
pattern file: picture_27
'''
import turtle           # allows us to use the turtles library
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle
alex.color("green")
alex.circle(50)
alex.circle(40)
alex.circle(30)
alex.circle(20)
alex.right(120)
alex.color("blue")
alex.circle(50)
alex.circle(40)
alex.circle(30)
alex.circle(20)
alex.right(120)
alex.color("red")
alex.circle(50)
alex.circle(40)
alex.circle(30)
alex.circle(20)
