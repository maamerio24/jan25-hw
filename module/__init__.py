# 2) Create a Module in Visual Studio Code and Import It
#     Module should have the following capabilities:

#     1) Has a function to calculate the square footage of a room
#     2) Has a function to calculate the circumference of a circle

#     Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

#     ** Note: When using functions in Python, arguments are passed in by reference, NOT value.

from math import pi


def circumference():
    radius = float(input("Please enter the radius of the circle. "))
    print("Your circumference is:")
    print(2 * pi * radius)


def area(w, l):
    w = float(input("What is the width of your room? "))
    l = float(input("What is the length of your room? "))
    print("The area of your room is:")
    print(w * l)