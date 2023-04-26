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
ball.dx = 0.05
ball.dy = -0.05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))

def paddle_One_up():
  y = paddleOne.ycor()
  y += 20
  paddleOne.sety(y)

def paddle_One_down():
  y = paddleOne.ycor()
  y -= 20
  paddleOne.sety(y)

def paddle_Two_up():
  y = paddleTwo.ycor()
  # y = y + 20
  y += 20 
  paddleTwo.sety(y)
  
def paddle_Two_down():
  y = paddleTwo.ycor()
  # y = y - 20
  y -= 20 
  paddleTwo.sety(y)

# Button Bindings
window.listen()
window.onkeypress(paddle_One_up, "w")
window.onkeypress(paddle_One_down, "s")
window.onkeypress(paddle_Two_up, "Up")
window.onkeypress(paddle_Two_down, "Down")

while True:
  window.update()

  ball.setx(ball.xcor()+ ball.dx)
  ball.sety(ball.ycor()+ ball.dy)

  # border checking
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1

  elif ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

  if ball.xcor() > 390:
    scoreA += 1
    pen.clear()
    pen.write("Player A: {} Player B{}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
    ball.goto(0,0)
    ball.dx *= -1

  elif ball.xcor() < -390:
    scoreB += 1
    pen.clear()
    pen.write("Player A: {} Player B{}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
    ball.goto(0,0)
    ball.dx *= -1


  if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddleTwo.ycor() + 40 and ball.ycor() > paddleTwo.ycor() -50:
     ball.setx(340)
     ball.dx *= -1

  elif (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddleOne.ycor() + 40 and ball.ycor() > paddleOne.ycor() -50: