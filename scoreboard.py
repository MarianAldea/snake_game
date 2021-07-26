from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.pencolor("black")
        self.speed("fastest")
        self.penup()
        with open("Data.txt",mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.scriere()
    def scriere(self):
        self.penup()
        self.goto(x=0, y=250)
        self.clear()
        self.pendown()
        self.pencolor("white")
        self.write(f"Score:{self.score}       High Score: {self.high_score}", True, align="center", font=("Arial", 16, "normal"))
        self.hideturtle()
        self.penup()

    def inc_score(self):
        self.score = self.score + 1
    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.pendown()
    #     self.write("Game Over", True, align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.clear()
            self.high_score = self.score
            with open("Data.txt", mode="w") as file:
                file.write(str(self.high_score))
            self.score = 0
            self.scriere()
        else:
            self.score = 0
            self.scriere()