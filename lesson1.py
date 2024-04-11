from turtle import *


#we want to paint a house

#step 1 draw a square

speed(10)
width(2)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(0, 200)
pendown()

color("yellow")
left(30)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(200, 200)
pendown()

left(180)
forward(50)
right(90)
forward(50)
right(90)
forward(50)














exitonclick()