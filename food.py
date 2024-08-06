from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.goto(100, 100)

    def new_food(self, rand_x, rand_y, rand_color):
        self.hideturtle()
        self.color(rand_color)
        self.goto(rand_x, rand_y)
        self.showturtle()
