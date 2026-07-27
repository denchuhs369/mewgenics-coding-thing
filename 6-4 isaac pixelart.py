s = "#fddfe4"
w = "white"
b = "black"
bl = "#67bed9"
pixelsize = 20
a = [w, w, w, w, w, b, b, b, b, w, w, w, w, w, w]
b = [w, w, w, w, b, s, s, s, s, b, w, w, w, w, w]
c = [w, w, w, b, s, s, s, s, s, s, b, w, w, w, w]
d = [w, w, b, s, s, b, s, s, b, s, s, b, w, w, w]
e = [w, w, b, s, s, bl, s, s, bl, s, s, b, w, w, w]
f = [w, w, b, s, s, bl, b, b, bl, s, s, b, w, w, w]
g = [w, w, b, s, s, b, w, w, b, s, s, b, w, w, w]
h = [w, w, w, b, s, b, b, b, b, s, b, w, w, w, w]
i1 = [w, w, w, w, b, s, s, s, s, b, w, w, w, w, w]
j = [w, w, b, b, s, s, s, s, s, s, b, b, b, w, w]
k = [w, b, s, s, s, s, s, s, s, s, s, s, s, b, w]
l = [b, s, s, b, b, s, s, s, s, s, b, b, s, s, b]
m = [b, s, b, w, b, s, s, s, s, s, b, w, b, s, b]
n = [b, s, b, w, b, s, s, s, s, s, b, w, b, s, b]
o = [w, b, w, w, b, s, s, s, s, s, b, w, w, b, w]
p = [w, w, w, w, b, s, b, b, b, s, b, w, w, w, w]
q = [w, w, w, w, b, s, b, w, b, s, b, w, w, w, w]
r = [w, w, w, w, b, b, b, w, b, b, b, w, w, w, w]
import turtle
t = turtle.Turtle()
turtle.tracer(0,0)
t.speed(0)
t.penup()
t.goto(-200, 200)
t.pendown()
for color in a:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(-200, 180)
t.pendown()
for color in b:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, 160)
t.pendown()
for color in c:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
  t.penup()
 
t.goto(-200, 140)
t.pendown()
for color in d:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, 120)
t.pendown()
for color in e:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, 100)
t.pendown()
for color in f:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, 80)
t.pendown()
for color in g:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, 60)
t.pendown()
for color in h:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, 40)
t.pendown()
for color in i1:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, 20)
t.pendown()
for color in j:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, 0)
t.pendown()
for color in k:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, -20)
t.pendown()
for color in l:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, -40)
t.pendown()
for color in m:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
 
t.goto(-200, -60)
t.pendown()
for color in n:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
t.goto(-200, -80)
t.pendown()
for color in o:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
t.goto(-200, -100)
t.pendown()
for color in p:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
t.goto(-200, -120)
t.pendown()
for color in q:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
t.goto(-200, -140)
t.pendown()
for color in r:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
turtle.update()
