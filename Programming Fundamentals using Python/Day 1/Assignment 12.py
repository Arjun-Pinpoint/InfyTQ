'''
Write a program to create the following pattern:
'''
import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
wn.setup(540,508)           # set window dimension

alex = turtle.Turtle()      # create a turtle named alex
alex.shape("turtle")        # alex looks like a turtle
alex.color('red')           # alex has a color
alex.circle(50)
alex.forward(100)
alex.backward(200)
alex.left(90)
alex.forward(100)
alex.right(90)
alex.forward(200)
alex.right(90)
alex.forward(100)
