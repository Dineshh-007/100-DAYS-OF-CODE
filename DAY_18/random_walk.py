from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
screen = Screen()
screen.title("Random Walk")
tim.speed("fastest")
colormode(255)    #----------------------> Dont forget to put this..or else you will get error bruh!!

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    my_tuple=(r,g,b)
    return my_tuple

tim.pensize(15)

for _ in range(100):
    tim.color(random_colour())
    tim.setheading(random.choice([0, 90, 180, 270]))  
    tim.forward(30)  # Move forward by 30 units

screen.mainloop()
