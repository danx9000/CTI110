# Drawing our initials
# CTI-110 P4T2 Initial 
# Daniel Choe
# 9/24/18


import turtle
#Drawing D
dword = turtle.Turtle()
dword.color("red")
dword.pensize("10")
dword.forward(50)
dword.left(45)
dword.forward(25)
dword.left(45)
dword.forward(100)
dword.left(45)
dword.forward(25)
dword.left(45)
dword.forward(50)
dword.left(90)
dword.forward(140)

#Lifting the pen up and move it so we won't overlap letters
cword = turtle.Turtle()

cword.penup()
cword.forward(175)
cword.pendown()

#Drawing C
cword.color("blue")
cword.pensize("10")
cword.backward(50)
cword.right(45)
cword.backward(25)
cword.right(45)
cword.backward(100)
cword.left(135)
cword.forward(25)
cword.right(45)
cword.forward(50)

# 1. Drawing D
# 2. lifting pen up using penup command
# 3. Drawing C


