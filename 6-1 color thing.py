import turtle
t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.setup(width=800, height=300)
colors = ["blue", "dark blue", "grey", "dark green", "light green"]
t.penup()
t.goto(-400, 150)
t.pendown()
for c in colors:
  t.color(c)
  t.begin_fill()
  t.forward(800)
  t.right(90)
  t.forward(60)
  t.left(90)
  t.forward(-800)
  t.end_fill()
