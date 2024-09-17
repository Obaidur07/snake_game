from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f'score: {self.score}', align='center', font=('Courier', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'score: {self.score}', align='center', font=('Courier', 18, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write(f'GAME OVER', align='center', font=('Courier', 14, 'normal'))
