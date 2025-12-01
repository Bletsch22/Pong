import turtle
import time
import random

# window
window = turtle.Screen()
window.title("pong")
window.bgcolor("black")
window.setup(width=1000, height=900)
window.tracer(0)

# Score
score_a = 0
score_b = 0

delay = 1

# Pen/Score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Paddle A left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()

# Give the ball a random direction
def reset_ball():
    ball.goto(0, 0)
    # random left/right and up/down
    ball.dx = random.choice([-0.14, 0.14])
    ball.dy = random.choice([-0.14, 0.14])

# --- AI CONFIG (slower paddles) ---
ai_speed_a = 0.20  # left paddle speed
ai_speed_b = 0.22  # right paddle speed

# Initialize ball direction once at start
reset_ball()

# main game loop
while True:

    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # borders (top/bottom)
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1

    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1

    # right side miss (Player A scores)
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write(
            "Player A: {} Player B: {}".format(score_a, score_b),
            align="center",
            font=("Courier", 24, "normal"),
        )
        reset_ball()
        time.sleep(delay)

    # left side miss (Player B scores)
    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(score_a, score_b),
            align="center",
            font=("Courier", 24, "normal"),
        )
        reset_ball()
        time.sleep(delay)

    # --- AI for paddle_b (right paddle) ---
    if ball.xcor() > 0:  # only chase when ball on right side
        if paddle_b.ycor() < ball.ycor() - 10:   # dead zone of 10
            paddle_b.sety(paddle_b.ycor() + ai_speed_b)
        elif paddle_b.ycor() > ball.ycor() + 10:
            paddle_b.sety(paddle_b.ycor() - ai_speed_b)

    # keep paddle_b inside the window
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    # --- AI for paddle_a (left paddle) ---
    if ball.xcor() < 0:  # only chase when ball on left side
        if paddle_a.ycor() < ball.ycor() - 10:
            paddle_a.sety(paddle_a.ycor() + ai_speed_a)
        elif paddle_a.ycor() > ball.ycor() + 10:
            paddle_a.sety(paddle_a.ycor() - ai_speed_a)

    # keep paddle_a inside the window
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    # paddle and ball collisions
    if (340 < ball.xcor() < 350) and (
        paddle_b.ycor() - 40 < ball.ycor() < paddle_b.ycor() + 40
    ):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (
        paddle_a.ycor() - 40 < ball.ycor() < paddle_a.ycor() + 40
    ):
        ball.setx(-340)
        ball.dx *= -1
