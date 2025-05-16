from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)

userbet=screen.textinput(title="Make your bet",prompt="Which turtle will win race? Enter a color")
print(userbet)

israce_on=False

colors=["red","orange","yellow","green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]

if userbet:
    israce_on=True

all_turtle=[]

for turtle_index in range(0,6):
    new_turtles=Turtle(shape="turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x=-230,y=y_position[turtle_index])
    new_turtles.pendown()
    all_turtle.append(new_turtles)

while israce_on:
    for turtle in all_turtle:
        if turtle.xcor() >= 230:     #-------> why not ==?? because turtle may not exactly land on 230...
            israce_on=False
            win_turtle = turtle.pencolor()
            if win_turtle == userbet:
                print(f"you won bruh....Your {win_turtle} won the race")
            else:
                print(f"Sorry You've Lost the game....{win_turtle} won the race")
        
        rand_distance=random.randint(0,10)
        turtle.penup()
        turtle.forward(rand_distance)
        turtle.pendown()
        
screen.mainloop()