import turtle
import random
t = turtle.Turtle()
t.speed(0)
boxes = []
random.shuffle(boxes)
screen = turtle.Screen()
wideness = int(input("What will your number of boxes be? (it has to be a multiple of 5)"))
screen.setup(width = (wideness * 100 + 50), height=300)
for i in range (wideness // 5):
  boxes.append("gold")
  boxes.append("bomb")
  boxes.append("gold")
  boxes.append("gold")
  boxes.append("gold")
random.shuffle(boxes)

t.speed(0)
theWidth = wideness * 100
thing = theWidth // 2 + 50
score = 0
t.penup()
t.goto(-thing, 0)
t.forward(50)
t.pendown()
for i in range(len(boxes)):
  for i in range(4):
    t.forward(50)
    t.right(90)
  t.penup()
  t.forward(100)
  t.pendown()
t.penup()
t.goto(-thing, 0)
t.forward(50)
t.pendown()
amount = 0
while True:
  box = input("What box do you want to choose?")
  box = int(box)
  if(boxes[box - 1]) == "x":
    print("You already chose that one!")
  if(boxes[box - 1]) == "gold":
    boxes[box - 1] = "x"
    print("gold!")
    t.penup()
    t.goto(-thing + 5,-32)
    t.forward(50)
    t.forward(100 * box)
    t.forward(-100)
    t.pendown()
    score+=1
    print("Score:" + str(score))
    t.write("💰", font=("Arial", 18, "normal"))
  if(boxes[box - 1]) == "bomb":
    print("bomb...")
    t.penup()
    t.goto(-thing + 5,-32)
    t.forward(50)
    t.forward(100 * box)
    t.forward(-100)
    t.pendown()
    t.write("💣", font=("Arial", 18, "normal"))
    print("Score:" + str(score))
    break

  
  amount+= 1
  if score == len(boxes) - 1:
    print "you won!"
    break
