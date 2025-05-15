from turtle import Turtle,Screen

tim = Turtle()
dash_length=20
dash_gap=15

for i in range(20):
    tim.forward(dash_length)
    tim.penup()
    tim.forward(dash_gap)
    tim.pendown()

screen=Screen()
screen.exitonclick()