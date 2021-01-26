# Classic PONG Game by Suryaansh Chawla
import turtle
# Window
wn=turtle.Screen()
wn.title("Pong by Suryaansh Chawla")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Main Game Loop
while True:
    wn.update()

# Paddles
# paddle a
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle_b
