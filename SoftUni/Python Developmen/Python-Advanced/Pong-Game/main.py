import turtle
import game
import time


STAMP_SIZE = 20
game = game.Game()

screen = turtle.Screen()
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)
screen.setup(game.width, game.height)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('green')
ball.penup()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(game.paddle_height / STAMP_SIZE, game.paddle_width / STAMP_SIZE)
paddle_a.penup()

while True:
    game.tick()
    ball.goto(game.ball_pos())
    paddle_a.goto(game.paddle_a_pos)
    screen.update()
    time.sleep(0.01)
