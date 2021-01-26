# Classic PONG Game by Suryaansh Chawla
import turtle
# Window
wn=turtle.Screen()
wn.title("Pong by Suryaansh Chawla")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)



# Paddles
# paddle Ka
paddleKa=turtle.Turtle()
paddleKa.speed(0)
paddleKa.shape("square")
paddleKa.color("darkorange")
paddleKa.shapesize(stretch_wid=5, stretch_len=1)
paddleKa.penup()
paddleKa.goto(-350, 0)

# paddle Ga
paddleGa=turtle.Turtle()
paddleGa.speed(0)
paddleGa.shape("square")
paddleGa.color("darkgreen")
paddleGa.shapesize(stretch_wid=5, stretch_len=1)
paddleGa.penup()
paddleGa.goto(350, 0)

# Ball(Genda is ball in Sanskrit)
Genda=turtle.Turtle()
Genda.speed(0)
Genda.shape("square")
Genda.color("blue")
Genda.shapesize(stretch_wid=1, stretch_len=1)
Genda.penup()
Genda.goto(0, 0)
Genda.dx=.5
Genda.dy=-.5

# Movement
# PaddleKa
def KaUp():
    y = paddleKa.ycor()
    y += 10
    paddleKa.sety(y)
def KaDown():
    y = paddleKa.ycor()
    y -= 10
    paddleKa.sety(y)

# PaddleGa
def GaUp():
    y = paddleGa.ycor()
    y += 10
    paddleGa.sety(y)

def GaDown():
    y = paddleGa.ycor()
    y -= 10
    paddleGa.sety(y)

wn.listen()
wn.onkeypress(KaUp, "w")
wn.onkeypress(KaDown, "s")
wn.onkeypress(GaDown, "Down")
wn.onkeypress(GaUp, "Up")

# Main Game Loop
while True:
    wn.update()
    # Move Genda
    Genda.setx(Genda.xcor() + Genda.dx)
    Genda.sety(Genda.ycor() + Genda.dy)

    # Bouncing the Genda
    if Genda.ycor() > 290:
        Genda.sety(290)
        Genda.dy*=-1

    if Genda.ycor() < -290:
        Genda.sety(-290)
        Genda.dy*=-1
# Classic PONG Game by Suryaansh Chawla
import turtle
# Window
wn=turtle.Screen()
wn.title("Pong by Suryaansh Chawla")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)



# Paddles
# paddle Ka
paddleKa=turtle.Turtle()
paddleKa.speed(0)
paddleKa.shape("square")
paddleKa.color("darkorange")
paddleKa.shapesize(stretch_wid=5, stretch_len=1)
paddleKa.penup()
paddleKa.goto(-350, 0)

# paddle Ga
paddleGa=turtle.Turtle()
paddleGa.speed(0)
paddleGa.shape("square")
paddleGa.color("darkgreen")
paddleGa.shapesize(stretch_wid=5, stretch_len=1)
paddleGa.penup()
paddleGa.goto(350, 0)

# Ball(Genda is ball in Sanskrit)
Genda=turtle.Turtle()
Genda.speed(0)
Genda.shape("square")
Genda.color("blue")
Genda.shapesize(stretch_wid=1, stretch_len=1)
Genda.penup()
Genda.goto(0, 0)
Genda.dx=.5
Genda.dy=-.5

# Movement
# PaddleKa
def KaUp():
    y = paddleKa.ycor()
    y += 10
    paddleKa.sety(y)
def KaDown():
    y = paddleKa.ycor()
    y -= 10
    paddleKa.sety(y)

# PaddleGa
def GaUp():
    y = paddleGa.ycor()
    y += 10
    paddleGa.sety(y)

def GaDown():
    y = paddleGa.ycor()
    y -= 10
    paddleGa.sety(y)

wn.listen()
wn.onkeypress(KaUp, "w")
wn.onkeypress(KaDown, "s")
wn.onkeypress(GaDown, "Down")
wn.onkeypress(GaUp, "Up")

# Main Game Loop
while True:
    wn.update()
    # Move Genda
    Genda.setx(Genda.xcor() + Genda.dx)
    Genda.sety(Genda.ycor() + Genda.dy)

    # Bouncing the Genda
    if Genda.ycor() > 290:
        Genda.sety(290)
        Genda.dy*=-1

    if Genda.ycor() < -290:
        Genda.sety(-290)
        Genda.dy*=-1
    if Genda.xcor() > 290:
        Genda.goto(0)
        Genda.dx*=-1
