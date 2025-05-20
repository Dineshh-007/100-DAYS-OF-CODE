from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")


screen.tracer(0)

snake=Snake()
#   snake.create_snake()   ---------->  if yuu need it here, you can put it here but remove it on __init__
food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.sixty,"6")
screen.onkey(snake.onethirtyfive,"5")
screen.onkey(snake.twotwentyfive,"4")


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.score_board()
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        score.score_update()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() >285 or snake.head.ycor() < -285 :
        game_is_on=False
        score.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10 :
            game_is_on=False
            score.game_over()

    
screen.exitonclick()