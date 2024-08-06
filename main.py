import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
import random

width = 500
height = 500
food_color = ['red', 'yellow', 'orange', 'green', 'pink']
s = Screen()
s.setup(width, height)
s.bgcolor('black')
s.title("Snake the game")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

snake.make_snake()
score.show_score()

s.listen()
s.onkey(fun=snake.up, key='Up')
s.onkey(fun=snake.down, key='Down')
s.onkey(fun=snake.left, key='Left')
s.onkey(fun=snake.right, key='Right')


def perimeter():
    perimeter_x = (width / 2) - 40
    perimeter_y = (height / 2) - 40
    if snake.snake_head.xcor() > perimeter_x or snake.snake_head.xcor() < -perimeter_x:
        return True
    elif snake.snake_head.ycor() > perimeter_y or snake.snake_head.ycor() < -perimeter_y:
        return True
    else:
        return False


def snake_eat_itself():
    if len(snake.snake_body) > 5:
        for square in snake.snake_body[2:]:
            if snake.snake_head.distance(square.xcor(), square.ycor()) < 5:
                return True


def get_random_food():
    x = random.randrange(-230, 230, 10)
    y = random.randrange(-230, 230, 10)
    color = random.choice(food_color)
    return {'x': x, 'y': y, 'color': color}


play = True
while play:
    if perimeter():
        snake.snake_head.color('red')
        score.game_over()
        play = False
    if snake_eat_itself():
        snake.snake_head.color('red')
        score.game_over()
        play = False
    if snake.snake_head.distance(food.xcor(), food.ycor()) < 20:
        rand_food_dict = get_random_food()
        food.new_food(rand_x=rand_food_dict['x'], rand_y=rand_food_dict['y'], rand_color=rand_food_dict['color'])
        score.increase_score()
        snake.make_snake()
    snake.move()
    s.update()
    time.sleep(0.1)

s.exitonclick()
