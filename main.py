import turtle
import os 

# Window setup
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height = 600)
window.tracer(0)

# Score variables
scoreA = 0
scoreB = 0

# Paddle 1
paddleOne = turtle.Turtle()
paddleOne.speed(0)
paddleOne.shape("square")
paddleOne.color("white")
paddleOne.shapesize(stretch_wid=5, stretch_len=-1)
paddleOne.penup()
paddleOne.goto(-350,0)

# Paddle 2
paddleTwo = turtle.Turtle()
paddleTwo.speed(0)
paddleTwo.shape("square")
paddleTwo.color("white")
paddleTwo.shapesize(stretch_wid=5, stretch_len=-1)
paddleTwo.penup()
paddleTwo.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))