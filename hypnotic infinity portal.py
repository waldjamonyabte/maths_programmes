import turtle, math

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")
t.color("cyan")

for i in range(500):
    t.forward(i/2)
    t.left(59)
    t.width(1 + i % 3)

turtle.done()
# source code --> clcoding.com