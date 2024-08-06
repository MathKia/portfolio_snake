from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def show_score(self):
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 200)
        self.write(f"Score: {self.score}", align="center", font=('Arial', 12, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(-100, 0)
        self.write(f"GAME OVER", font=('Arial', 20, 'bold'))
        self.goto(-100, -30)
        self.write(f'Final score: {self.score}', font=('Arial', 14, 'bold'))
