# Cade Sayner SYNCAD001
# A program to draw a text based graph of a function f(x)
# 22/03/2022 

import math
input_ = input("Enter a function f(x): \n")
for y in range(10, -11, -1): # Loop from the top left corner down
    for x in range(-10, 12):
        if y == round(eval(input_)) and x != 11: # if the function value is equal to the current y value print "o"
            print("o", end = "")
        elif x == 0 and y == 0: # if the x and y coordinates are the origin then print "+"
            print("+", end = "")
        elif x == 0:
            print("|", end = "") # if the x c oordinated are 0, draw th y axis by printing a '|'
        elif x == 11: # Print a new line if x is equal to 11
            print()
        elif  y == 0: # Print out the x axis using '-' if the current value is equal to 0
            print("-", end = "")
        else:
            print(" ", end= "") # if none of the above conditions are met, simply print an empty string.


        
