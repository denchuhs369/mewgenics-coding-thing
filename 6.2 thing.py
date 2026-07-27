import turtle
import random
t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.setup(width=800, height=300)
colors = []
shapes = []
while True:
  answer = input("Enter a color, enter \"stop\" to stop")
  if answer == "stop":
    break
  else:
    colors.append(answer)
print(colors)
while True:
  answer = input("Now, enter the shapes you want.")
  if answer == "stop":
    break
  else:
    shapes.append(answer)
print (shapes)
for s in shapes:
  t.color(random.choice(colors))
  t.shape(s)
  t.stamp()
  t.penup()
  t.forward(100)
  t.pendown()
