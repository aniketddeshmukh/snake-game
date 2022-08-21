from turtle import Screen,Turtle
import time
from Snake import snake
from food import *
from Scoreboard import *

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

Saanp = snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Saanp.up,"Up")
screen.onkey(Saanp.down,"Down")
screen.onkey(Saanp.left,"Left")
screen.onkey(Saanp.right,"Right")


game_is_on =True
while game_is_on:
    Screen().update()
    time.sleep(0.1)
    Saanp.move()
    #Collision with food
    if Saanp.head.distance(food)<15:
        food.refresh()
        Saanp.extend()
        scoreboard.increase_score()

    #Collision with wall
    if Saanp.head.xcor() >280 or Saanp.head.xcor() < -280 or Saanp.head.ycor() > 280 or Saanp.head.xcor() < -280:
        game_is_on =False
        scoreboard.game_over()
        
    #Collision with  tail
    for segment in Saanp.segments[1:]:
        if Saanp.head.distance(segment)<10:
            game_is_on =False
            scoreboard.game_over()

