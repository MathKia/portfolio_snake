import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
import random

# Set up screen dimensions and food colors
width = 500
height = 500
food_color = ['red', 'yellow', 'orange', 'green', 'pink']

# Initialize the game screen
s = Screen()
s.setup(width, height)
s.bgcolor('black')
s.title("Snake the game")
s.tracer(0)  # Disable automatic updates for smooth animation


def perimeter():
    """Check if the snake hits the game boundary."""
    perimeter_x = (width / 2) - 40
    perimeter_y = (height / 2) - 40
    return (
        snake.snake_head.xcor() > perimeter_x or
        snake.snake_head.xcor() < -perimeter_x or
        snake.snake_head.ycor() > perimeter_y or
        snake.snake_head.ycor() < -perimeter_y
    )


def snake_eat_itself():
    """Check if the snake collides with its own body."""
    if len(snake.snake_body) > 5:
        for square in snake.snake_body[2:]:  # Ignore head and first segment
            if snake.snake_head.distance(square.xcor(), square.ycor()) < 5:
                return True
    return False


def get_random_food():
    """Generate a random food position and color."""
    x = random.randrange(-230, 230, 10)
    y = random.randrange(-230, 230, 10)
    color = random.choice(food_color)
    return {'x': x, 'y': y, 'color': color}


def reset_game():
    """Reset the game state for replay."""
    global snake, food, score
    s.clear()
    s.bgcolor('black')
    s.title("Snake the game")
    s.tracer(0)

    # Reinitialize game objects
    snake = Snake()
    food = Food()
    score = Score()
    score.show_score()

    # Rebind controls
    s.listen()
    s.onkey(fun=snake.up, key='Up')
    s.onkey(fun=snake.down, key='Down')
    s.onkey(fun=snake.left, key='Left')
    s.onkey(fun=snake.right, key='Right')

    play_game()


def play_game():
    """Main game loop that runs until the player loses."""
    global snake, food, score

    snake.make_snake()
    score.show_score()
    play = True

    while play:
        # Check for collisions with walls or itself
        if perimeter() or snake_eat_itself():
            snake.snake_head.color('red')
            score.game_over()
            play = False
            break  # Stop the game loop

        # Check if snake eats food
        if snake.snake_head.distance(food.xcor(), food.ycor()) < 20:
            rand_food_dict = get_random_food()
            food.new_food(rand_x=rand_food_dict['x'], rand_y=rand_food_dict['y'], rand_color=rand_food_dict['color'])
            score.increase_score()
            snake.make_snake()  # Grow the snake

        snake.move()
        s.update()
        time.sleep(0.1)

    # Wait for replay input
    s.onkey(reset_game, 'y')  # Restart game if 'y' is pressed
    s.onkey(end_game, 'n')  # Exit game if 'n' is pressed
    s.listen()  # Ensure keypresses are detected


def end_game():
    """Exit the game."""
    s.bye()


# Initialize game objects
snake = Snake()
food = Food()
score = Score()

# Bind controls for snake movement
s.listen()
s.onkey(fun=snake.up, key='Up')
s.onkey(fun=snake.down, key='Down')
s.onkey(fun=snake.left, key='Left')
s.onkey(fun=snake.right, key='Right')

# Start the game loop
play_game()
s.mainloop()  # Keep the game window open