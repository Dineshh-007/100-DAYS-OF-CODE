from turtle import Turtle,Screen,colormode
import random

tim=Turtle()
colormode(255)
screen=Screen()
def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    my_colour=(r,g,b)
    return my_colour

tim.speed("fastest")
def spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        current_heading=tim.heading()
        tim.setheading(current_heading+size_of_gap)

spirograph(5)

screen.mainloop()