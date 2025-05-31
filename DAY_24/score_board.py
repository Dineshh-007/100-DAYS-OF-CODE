from turtle import Turtle
ALIGNMENT="center"
FONT =("Courier",24,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)  
        self.color("white")
        self.score_board()

    def score_board(self):
        self.clear()
        with open("data.txt") as file:
            c=file.read()
        self.write(f"SCORE = {self.score} HIGHSCORE = {c} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.score_board()

    def score_increase(self):
        self.score+=1
        self.score_board()