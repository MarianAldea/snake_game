from turtle import Screen
import time
import snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Game of snake")
mancare = 0

x_coord = 0
segment_list = []
screen.tracer(0)

snake = snake.Snake("green",4)
score = Score()
food = Food()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
screen.onkey(snake.down,"s")
screen.update()
game_is_on = True

while game_is_on:
    screen.listen()
    screen.update()
    time.sleep(0.1)
    snake.forward()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.inc_score()
        score.scriere()
        snake.extend("green")

    if snake.head.xcor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        score.reset()
        snake.reset()

    for segment in snake.segment_list[3:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()











screen.exitonclick()