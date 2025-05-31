from turtle import Turtle

POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]   # -------> to just point the snake's head


    def create_snake(self):
        for positions in POSITIONS:
            self.add_segments(positions)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



    def add_segments(self,positions):
            new_snake=Turtle()
            new_snake.color("white")
            new_snake.shape("square")
            new_snake.penup()
            new_snake.goto(positions)
            self.segments.append(new_snake)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:   # -------> heading()
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def sixty(self):
        self.head.setheading(60)

    def onethirtyfive(self):
        self.head.setheading(135)   

    def twotwentyfive(self):
        self.head.setheading(225)  