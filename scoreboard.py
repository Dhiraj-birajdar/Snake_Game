from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -10)
        self.write("Project by Dhiraj Birajdar", align=ALIGNMENT, font=("comic sans", 10, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)
