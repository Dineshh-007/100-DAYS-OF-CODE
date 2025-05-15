from turtle import Turtle,Screen
import random

tim=Turtle()

diff_color=["Blue","Red","Yellow","DarkOrchid"]

for n in range(3,11):
    tim.color(random.choice(diff_color))
    angle=360/n
    for i in range(0,n):
        tim.forward(100)
        tim.right(angle)

screen=Screen()
screen.exitonclick()