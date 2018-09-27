# Draw a square loop
# Date
# CTI-110 P4LAB - Nested Loop
# Daniel Choe
#

import turtle 
# start of loop
wow = turtle.Turtle()
wow.speed(20)
wow.color('red')
# loop 150 times
for i in range(150):
    wow.forward(i * 2)
    wow.right(90)

turtle.done()

# Draw a square line 150 times
