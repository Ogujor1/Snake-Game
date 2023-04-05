from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=510, height=510)
screen.bgcolor('black')

# Creating the snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# Call the listening key
screen.listen()
screen.onkeypress(snake.up(), 'up')
screen.onkeypress(snake.down(), 'down')
screen.onkeypress(snake.right(), 'right')
screen.onkeypress(snake.left(), 'left')

# moving the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 248 or snake.head.xcor() < -248 or snake.head.ycor() > 248 or snake.head.ycor() < -248:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with body
    for segment in snake.all_segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()