import turtle
import time
import winsound

#window
window = turtle.Screen()
window.title("pong")
window.bgcolor("black")
window.setup(width = 800, height=600)
window.tracer(0)

#Score
score_a = 0
score_b = 0

delay = 1

#Pen/Score board

pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle() 
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = "center", font=("Courier", 24, "normal"))

#Paddle A left

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid = 5, stretch_len =1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B right

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid = 5, stretch_len =1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()

#function Paddle A left

def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

#keyboard binding paddle A

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")


#function Paddle B right
def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

#keyboard binding Paddle B

window.listen()
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

#ball movement function
ball.dx = 0.17
ball.dy = 0.17 


# main game loop

while True:

  window.update()
  
  #moving the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  #borders
  if ball.ycor() > 290:
     ball.sety(290)
     ball.dy *= -1
     winsound.PlaySound("Pong paddle.wav", winsound.SND_ASYNC)
     

  if ball.ycor() < -290:
     ball.sety(-290)
     ball.dy *= -1 
     winsound.PlaySound("Pong paddle.wav", winsound.SND_ASYNC)


  if ball.xcor() > 390:
     ball.goto(0,0)
     score_a += 1
     pen.clear()
     pen.write("Player A: {} Player B: {}".format(score_a,score_b), align = "center", font=("Courier", 24, "normal"))
     time.sleep(delay)
     

  if ball.xcor() < -390:
     ball.goto(0,0)
     score_b += 1
     pen.clear()
     pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align = "center", font=("Courier", 24, "normal"))
     time.sleep(delay)  
     

 
  #paddle and ball collisions
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):   
      ball.setx(340)
      ball.dx *= -1
      winsound.PlaySound("Paddle.wav", winsound.SND_ASYNC)


  if (ball.xcor()< -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+ 40 and ball.ycor() > paddle_a.ycor() -40):   
      ball.setx(-340)
      ball.dx *= -1 
      winsound.PlaySound("Paddle.wav", winsound.SND_ASYNC)

