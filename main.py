# Pong implemented in Python using Turtle for the GUI stuff
# made following https://www.youtube.com/watch?v=XGf2GcyHPhc&t=78s

import turtle

window = turtle.Screen() #create window object
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

while True:
    window.update()