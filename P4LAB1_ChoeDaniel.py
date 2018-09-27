# CREATING A SQUARE AND A TRIANGLE
# CTI-110 P4T1_TURTLE GRAPHICS
# Daniel Choe
# 9/24/18

import turtle

# Creating a square
square = turtle.Turtle()

square.shape("turtle")
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)

# Creating a Triangle
triangle = turtle.Turtle()

triangle.shape("turtle")
triangle.forward(200)
triangle.left(120)
triangle.forward(80)
triangle.left(120)
triangle.forward(80)
# window exit if you click on it
turtle.exitonclick()

# 1. naming a code square
# 2. the square is created by code
# 3. repeat step 1 but it's a triangle
# 4. the triangle is  created by code
# 5. exit on click
