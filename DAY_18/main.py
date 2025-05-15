from turtle import Turtle,Screen

# if you want go give alias name to turtle then  ---> import turtle as t

tim=Turtle()
tim.shape("turtle")
tim.color("blue")
tim.pencolor("red")


for _ in range(4):
    tim.fd(100)
    tim.right(90)


screen = Screen()
screen.bgcolor("orange")
screen.exitonclick()


# How to install any packages
# import heroes
# print(heroes.gen())
# import villains
# print(villains.gen())
