from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self. l_score=0
        self.r_score=0

        self.update()
    def update(self):
        self.clear()
        self.goto(-200, 250)
        self.write(self.l_score,align="Center",font=('Courier',40,'normal'))
        self.goto(200,250)
        self.write(self.r_score, align="Center", font=('Courier', 40, 'normal'))
    def update_right(self):
        self.r_score+=1
        self.update()

    def update_left(self):
        self.l_score+=1
        self.update()
