from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_body = []
        self.make_snake()
        self.snake_head = self.snake_body[0]
        self.snake_head.turtlesize(stretch_len=2)
        self.snake_head.color('white')

    def make_snake(self):
        if len(self.snake_body) == 0:
            x_pos = 0
            for _ in range(3):
                snake_square = Turtle()
                snake_square.penup()
                snake_square.shape('square')
                snake_square.color('green')
                snake_square.goto(0 + x_pos, 0)
                self.snake_body.append(snake_square)
                x_pos += 40
        else:
            for _ in range(2):
                snake_square = Turtle()
                snake_square.shape('square')
                snake_square.color('green')
                snake_square.penup()
                self.move()
                self.snake_body.append(snake_square)



    def move(self):
        head_x = self.snake_head.xcor()
        head_y = self.snake_head.ycor()
        self.snake_head.forward(10)
        for square in self.snake_body[1:]:
            square_x = square.xcor()
            square_y = square.ycor()
            square.goto(head_x, head_y)
            head_x = square_x
            head_y = square_y

    def left(self):
        current_direction = self.snake_head.heading()
        if current_direction == 90 or current_direction == 270:
            self.snake_head.setheading(180)
            self.move()

    def right(self):
        current_direction = self.snake_head.heading()
        if current_direction == 90 or current_direction == 270:
            self.snake_head.setheading(0)
            self.move()

    def up(self):
        current_direction = self.snake_head.heading()
        if current_direction == 180 or current_direction == 0:
            self.snake_head.setheading(90)
            self.move()

    def down(self):
        current_direction = self.snake_head.heading()
        if current_direction == 180 or current_direction == 0:
            self.snake_head.setheading(270)
            self.move()
