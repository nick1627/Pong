# Pong implemented in Python using Turtle for the GUI stuff, veeery beginner level
# made following https://www.youtube.com/watch?v=XGf2GcyHPhc&t=78s

import turtle
import os
import time

window = turtle.Screen() #create window object
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
# set animation speed to max possible
paddleA.speed(0)
paddleA.shape("square") #default size 20x20 pixels
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0) #set initial position


# Paddle B
paddleB = turtle.Turtle()
# set animation speed to max possible
paddleB.speed(0)
paddleB.shape("square") #default size 20x20 pixels
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0) #set initial position


# Ball
ball = turtle.Turtle()
# set animation speed to max possible
ball.speed(0)
ball.shape("square") #default size 20x20 pixels
ball.color("white")
ball.penup()
ball.goto(0, 0) #set initial position
ball.dx = 1 #every time ball moves, it moves 2 pixels
ball.dy = 1



# Functions
def paddleAUp():
    y = paddleA.ycor() #get y coord of paddle
    y += 20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor() #get y coord of paddle
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor() #get y coord of paddle
    y += 20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor() #get y coord of paddle
    y -= 20
    paddleB.sety(y)

def updateScore():
    pen.clear()
    pen.write("Computer: {}  Player: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

def makeBounceNoise():
    os.system("afplay Pong_bounce.wav&")
    return


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
updateScore()


# keyboard binding
window.listen() #tell the window to listen for inputs
window.onkeypress(paddleAUp, "w")
window.onkeypress(paddleADown, "s")
window.onkeypress(paddleBUp, "Up")
window.onkeypress(paddleBDown, "Down")

# main game loop
while True:
    # time.sleep(0.003)
    window.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        makeBounceNoise()


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        makeBounceNoise()


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        updateScore()


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        updateScore()

    
    # paddle and ball collition
    if ball.xcor() > 340 and ball.xcor() < 350:
        if ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
            # we should bounce
            ball.setx(340)
            ball.dx *= -1
            makeBounceNoise()

    if ball.xcor() < -340 and ball.xcor() > -350:
        if ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50:
            # we should bounce
            ball.setx(-340)
            ball.dx *= -1
            makeBounceNoise()

    # computer player
    if paddleA.ycor() < ball.ycor() and abs(paddleA.ycor() - ball.ycor()) > 10:
        paddleAUp()
    elif paddleA.ycor() > ball.ycor() and abs(paddleA.ycor() - ball.ycor()) > 10:
        paddleADown()
    
