from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard
import time
sc=Screen()
sc.tracer(0)
score=Scoreboard()
sc.bgcolor("black")
sc.setup(height=600,width=800)
sc.title("pong game")
pa_right=Paddle(380)
pa_left=Paddle(-390)
b=Ball()
sc.listen()
sc.onkeypress(pa_right.go_up,"Up")
sc.onkeypress(pa_right.down,"Down")
sc.onkeypress(pa_left.go_up,"W")
sc.onkeypress(pa_left.down,"S")
Game_is_on=True
while Game_is_on:
    time.sleep(0.1)
    sc.update()
    if b.ycor()>280 or b.ycor()<-280:
        b.bounce_y()
    if b.distance(pa_right)<50 and b.xcor()>360 or b.distance(pa_left)<50 and b.xcor()<-370:
        b.bounce_x()
    if b.xcor()>380 and b.distance(pa_right)>50:
        b.goto(0,0)
        b.bounce_x()
        score.update_left()
    if b.xcor()<-380 and b.distance(pa_left)>50:
        b.goto(0,0)
        b.bounce_x()
        score.update_right()

    b.move()



sc.exitonclick()
