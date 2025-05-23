from turtle import Turtle,Screen
from paddles import Paddles
import time
from ball import Ball
from scoreboard import Scoreboard
screen=Screen()

screen.setup(width=800,height=600)
screen.bgcolor("Black")
screen.title("The Ping Pong Game")
screen.tracer(0)

r_paddle=Paddles((350,0))
l_paddle=Paddles((-350,0))
ball =Ball()

is_gameon=True
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

scoreboard=Scoreboard()

while is_gameon:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320 :
        ball.bounce_x()
        
    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_scores()
        
    if ball.xcor() < -380:
        scoreboard.r_scores()
        ball.reset_position()
        
        
screen.exitonclick()