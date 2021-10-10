# Christmas Tree using Turtle

#!/usr/bin/python3.6
import numpy as np
import turtle
from turtle import *
#import Tkinter 

speed(0)

# image background
penup()
goto(0, -250)
pendown()
color('skyblue')
begin_fill()
circle(250)
end_fill()

# Tree
penup()
goto(-15, -50)
pendown()
color('brown')
begin_fill()

for i in range(2):
	forward(30)
	right(90)
	forward(40)
	right(90)

end_fill() 

# branches

y = -50  # tree trunk
width = 240
height = 25

while width > 20:
	width = width - 30 # makeing the tree smaller as it goes up
	x = 0 - width / 2  # set x values for each level of tree
	color('green')
	goto(x,y)
	pendown()
	begin_fill()
	for i in range(2):
		forward(width)
		left(90)
		forward(height)
		left(90)
	end_fill()
	
	y = y + height

#star

penup()
goto(-15, 150)
pendown()
color('yellow')
begin_fill()
for i in range(5):
	forward(30)
	right(144)
end_fill()
	
penup()
goto(-130, -150)
pendown()	
color('red')
write("MERRY CHRISTMAS", font=("Arial", 20, "bold"))\

hideturtle()
turtle.mainloop()
ts = turtle.getscreen()
ts.getcanvas().postscript(file="tree.png")	
	
