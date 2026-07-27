import turtle
def draw(x,y, size, pixelrows):
  for row in pixelrows:
    t.goto(x, y)
    y -= size
    t.pendown()
    for color in row:
      t.color(color)
      t.begin_fill()
      for i in range (4):
        t.forward(size)
        t.right(90)
      t.end_fill()
      t.forward(size)
    t.penup()
  t.update()

tank = "#847348"
mage = "#787898"
thief = "#fefab4"
cleric = "#f5f3f3"
fighter = "#b07373"
hunter = "#425d3d"
necromancer = "#212121"
psychic = "#645379"
engineer = "#96deca"
butcher = "#ab4457"
druid = "#4d362d"
colarless = "#cdccc8"
monk = "#a1a1a1"
fly = "fly"
championfly = "championfly"
dip = "dip"
rat = "rat"
spiderling = "spiderling"
snake = "snake"
wisp = "wisp"
championwisp = "championwisp"
screen = turtle.Screen()
screen.setup(width = 1000, height = 500)
cats = [tank, mage, thief, cleric, fighter, hunter, necromancer, psychic, engineer, butcher, druid, colarless, monk]
enemy = [fly, championfly, dip, rat, spiderling, snake, wisp, championwisp]
import random
cat1 = random.choice(cats)
print(cat1)
enemy1 = random.choice(enemy)
print(enemy1)
b = "black"
w = "white"
wo = "#424242"
wi = "#bdbdbd"
fl = "#212121"
an = "#0a0a0a"
c = (cat1)
e = "#ffcdd2"
dd = "#5a423c"
dl = "#96756c"
d = "#74564e"
#fly pixels
fly = [w, w, w, wo, w, w, w, w, w, w, w, w, w, w, wo, w, w, w]
fly2 = [w, w, wo, wi, wo, w, w, w, w, w, w, w, w, wo, wi, wo, w, w]
fly3 = [w, wo, wi, wi, wi, wo, w, w, w, w, w, w, wo, wi, wi, wi, wo, w]
fly4 = [wo, wi, wi, wi, wi, wi, wo, w, w, w, w, wo, wi, wi, wi, wi, wi, wo]
fly5 = [w, wo, wi, wi, wi, wi, b, b, b, b, b, b, wi, wi, wi, wi, wo, w]
fly6 = [w, w, wo, wi, wi, b, fl, fl, fl, fl, fl, fl, b, wi, wi, wo, w, w]
fly7 = [w, w, w, wo, wi, b, fl, fl, fl, fl, fl, fl, b, wi, wo, w, w, w]
fly8 = [w, w, w, w, wo, b, fl, fl, fl, fl, fl, fl, b, wo, w, w, w, w]
fly9 = [w, w, w, w, w, b, fl, fl, fl, fl, fl, fl, b, w, w, w, w, w]
fly10 = [w, w, w, w, w, b, fl, fl, fl, fl, fl, fl, b, w, w, w, w, w]
fly11 = [w, w, w, w, w, b, fl, fl, fl, fl, fl, fl, b, w, w, w, w, w]
fly12 = [w, w, w, w, w, w, b, b, b, b, b, b, w, w, w, w, w, w]
flyall = [fly, fly2, fly3, fly4, fly5, fly6, fly7, fly8, fly9, fly10, fly11, fly12]

#championfly pixels
champfly = [w, w, w, w, w, wo, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, wo, w, w, w, w, w]
champfly2 = [w, w, w, w, wo, wi, wo, w, w, w, w, w, w, w, w, w, w, w, w, w, w, wo, wi, wo, w, w, w, w]
champfly3 = [w, w, w, wo, wi, wi, wi, wo, w, w, w, w, w, w, w, w, w, w, w, w, wo, wi, wi, wi, wo, w, w, w]
champfly4 = [w, w, wo, wi, wi, wi, wi, wi, wo, w, w, w, w, w, w, w, w, w, w, wo, wi, wi, wi, wi, wi, wo, w, w]
champfly5 = [w, wo, wi, wi, wi, wi, wi, wi, b, b, w, w, w, w, w, w, w, w, b, b, wi, wi, wi, wi, wi, wi, wo, w]
champfly6 = [wo, wi, wi, wi, wi, wi, wi, wi, b, b, wo, w, w, w, w, w, w, wo, b, b, wi, wi, wi, wi, wi, wi, wi, wo]
champfly7 = [w, wo, wi, wi, wi, wi, wi, wi, wi, b, b, wo, w, w, w, w, wo, b, b, wi, wi, wi, wi, wi, wi, wi, wo, w]
champfly8 = [w, w, wo, wi, wi, wi, wi, wi, wi, b, b, b, b, b, b, b, b, b, b, wi, wi, wi, wi, wi, wi, wo, w, w]
champfly9 = [w, w, w, wo, wi, wi, wi, wi, b, fl, an, an, fl, fl, fl, fl, an, an, fl, b, wi, wi, wi, wi, wo, w, w, w]
champfly10 = [w, w, w, w, wo, wi, wi, wi, b, fl, fl, an, an, fl, fl, an, an, fl, fl, b, wi, wi, wi, wo, w, w, w, w]
champfly11 = [w, w, w, w, w, wo, wi, wi, b, fl, fl, fl, an, an, an, an, fl, fl, fl, b, wi, wi, wo, w, w, w, w, w]
champfly12 = [w, w, w, w, w, w, wo, wi, b, fl, fl, fl, fl, an, an, fl, fl, fl, fl, b, wi, wo, w, w, w, w, w, w]
champfly13 = [w, w, w, w, w, w, w, wo, b, fl, fl, fl, fl, fl, fl, fl, fl, fl, fl, b, wo, w, w, w, w, w, w, w]
champfly14 = [w, w, w, w, w, w, w, w, b, fl, fl, fl, fl, fl, fl, fl, fl, fl, fl, b, w, w, w, w, w, w, w, w]
champfly15 = [w, w, w, w, w, w, w, w, b, fl, fl, fl, fl, fl, fl, fl, fl, fl, fl, b, w, w, w, w, w, w, w, w]
champfly16 = [w, w, w, w, w, w, w, w, b, fl, fl, fl, fl, fl, fl, fl, fl, fl, fl, b, w, w, w, w, w, w, w, w]
champfly17 = [w, w, w, w, w, w, w, w, b, fl, fl, fl, fl, fl, fl, fl, fl, fl, fl, b, w, w, w, w, w, w, w, w]
champfly18 = [w, w, w, w, w, w, w, w, w, b, b, b, b, b, b, b, b, b, b, w, w, w, w, w, w, w, w, w]
champflyall = [champfly, champfly2, champfly3, champfly4, champfly5, champfly6, champfly7, champfly8, champfly9,
champfly10, champfly11, champfly12, champfly13, champfly14, champfly15, champfly16, champfly17, champfly18]

#cat pixels
cat = [w, w, b, w, w, w, w, w, w, w, w, w, w, w, b, w, w, w, w, w, w, w, w, w, w]
cat2 = [w, b, e, b, w, w, w, w, w, w, w, w, w, b, e, b, w, w, w, w, w, w, w, w, w]
cat3 = [b, e, e, e, b, w, w, w, w, w, w, w, b, e, e, e, b, w, w, w, w, w, w, w, w]
cat4 = [b, e, e, e, e, b, w, w, w, w, w, b, e, e, e, e, b, w, w, w, w, w, w, w, w]
cat5 = [b, e, e, b, b, b, b, b, b, b, b, b, b, b, e, e, b, w, w, w, w, w, w, w, w]
cat6 = [b, e, b, c, c, c, c, c, c, c, c, c, c, c, b, e, b, w, w, w, w, w, w, w, w]
cat7 = [b, b, c, c, c, c, c, c, c, c, c, c, c, c, c, b, b, w, w, w, w, w, w, w, w]
cat8 = [b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, w, w, w, w, w, w, w, w]
cat9 = [b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, w, w, w, w, w, w, w, w]
cat10 = [b, c, b, b, c, c, c, c, c, c, c, c, c, b, b, c, b, w, w, w, w, w, w, w, w]
cat11 = [b, c, b, b, c, b, c, c, b, c, c, b, c, b, b, c, b, w, w, w, w, w, w, w, w]
cat12 = [b, c, c, c, c, b, c, c, b, c, c, b, c, c, c, c, b, w, w, w, w, w, w, w, w]
cat13 = [b, c, c, c, c, b, b, b, b, b, b, b, c, c, c, c, b, w, w, w, w, w, w, w, w]
cat14 = [b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, w, w, w, w, w, b, b, b]
cat15 = [b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, w, w, w, w, b, c, c, b]
cat16 = [w, b, c, c, c, c, c, c, c, c, c, c, c, c, c, b, w, w, w, w, b, c, c, c, b]
cat17 = [w, w, b, c, c, c, c, c, c, c, c, c, c, c, b, b, b, b, b, b, c, c, c, b, w]
cat18 = [w, w, w, b, b, b, b, b, b, b, b, b, b, b, c, c, c, c, c, b, c, c, b, w, w]
cat19 = [w, w, w, b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, b, w, w, w]
cat20 = [w, w, w, b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, w, w, w, w]
cat21 = [w, w, w, w, b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, w, w, w, w]
cat22 = [w, w, w, w, b, b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, w, w, w, w]
cat23 = [w, w, w, b, b, b, b, c, c, c, c, c, c, c, c, c, c, c, c, b, w, w, w, w, w]
cat24 = [w, w, b, b, b, w, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, w, w, w]
cat25 = [w, w, b, b, w, w, b, b, b, w, w, w, w, b, b, w, w, w, w, b, b, b, w, w, w]
cat26 = [w, w, w, w, w, b, b, b, w, w, w, w, w, b, b, b, w, w, w, w, b, b, b, w, w]
cat27 = [w, w, w, w, w, b, b, w, w, w, w, w, w, w, b, b, w, w, w, w, w, b, b, w, w]

#dip pixels
dip = [w, w, w, w, w, w, w, w, b, w, w, w, w, w, w, w, w]
dip2 = [w, w, w, w, w, w, w, b, b, b, w, w, w, w, w, w, w,]
dip3 = [w, w, w, w, w, w, b, b, dd, b, b, w, w, w, w, w, w,]
dip4 = [w, w, w, w, w, b, b, dd, d, dd, b, b, w, w, w, w, w,]
dip5 = [w, w, w, w, b, b, dl, dl, d, d, dd, b, b, w, w, w, w,]
dip6 = [w, w, w, w, b, b, dl, dl, d, d, d, dd, b, b, w, w, w,]
dip7 = [w, w, w, b, b, d, dl, dl, d, d, d, d, dd, b, b, w, w,]
dip8 = [w, w, w, b, b, dl, dl, dl, d, d, d, d, d, b, b, w, w,]
dip9 = [w, w, b, b, d, dl, dl, dl, d, d, d, d, d, dd, b, b, w,]
dip10 = [w, b, b, d, dl, dl, dl, dl, d, d, d, d, d, d, b, b, w,]
dip11 = [w, b, b, dl, dl, b, dl, dl, d, d, d, d, b, d, b, b, w,]
dip12 = [b, b, dd, dl, dl, dl, dl, d, d, d, d, d, d, d, dd, b, b]
dip13 = [b, b, d, d, dl, b, b, b, b, b, b, b, b, d, d, b, b]
dip14 = [b, b, d, d, d, b, b, b, b, b, b, b, b, d, d, b, b]
dip15 = [b, b, d, d, d, b, b, b, b, b, b, b, b, d, d, b, b]
dip16 = [b, b, d, d, d, b, b, b, b, b, b, b, b, d, d, b, b]
dip17 = [b, b, dd, d, d, d, b, b, b, b, b, b, d, d, dd, b, b]
dip18 = [w, b, b, dd, d, d, d, d, d, d, d, d, d, dd, b, b, w]
dip19 = [w, w, b, b, b, dd, dd, dd, dd, dd, dd, dd, b, b, b, w, w]
dip20 = [w, w, w, b, b, b, b, b, b, b, b, b, b, b, w, w, w]
dip21 = [w, w, w, w, w, b, b, b, b, b, b, b, w, w, w, w, w]
dipall = [dip, dip2, dip3, dip4, dip5, dip6, dip7, dip8, dip9, dip10, dip11, dip12, dip13, dip14, dip15, 
dip16, dip17, dip18, dip19, dip20, dip21]

import turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
gotoy = 200
t.goto(0, 200)
t.pendown()

#cat printing
turtle.tracer(0,0)
pixelsize = 8
gotoy = 192
for color in cat:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, 192)
gotoy -= pixelsize
t.pendown()
for color in cat2:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat3:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat4:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat5:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat6:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat7:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat8:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat9:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat10:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat11:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat12:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat13:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat14:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat15:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat16:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
  
t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat17:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat18:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat19:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat20:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat21:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat22:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat23:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat24:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat25:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat26:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()

t.goto(0, gotoy)
gotoy -= pixelsize
t.pendown()
for color in cat27:
  t.color(color)
  t.begin_fill()
  for i in range (4):
    t.forward(pixelsize)
    t.right(90)
  t.end_fill()
  t.forward(pixelsize)
t.penup()
turtle.update()

#dip printing
turtle.tracer(0,0)
if enemy1 == "dip":
  draw(-375, 200, 12.5, dipall)
  
  
  '''
  pixelsize = 12.5
  t.goto(-375, 200)
  gotoy = 187.5
  t.pendown()
  for color in dip:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip2:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip3:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip4:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip5:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip6:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip7:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip8:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip9:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip10:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip11:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip12:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip13:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip14:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip15:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip16:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip17:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip18:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip19:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip20:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in dip21:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  turtle.update()
  '''
#champion fly printing
turtle.tracer(0,0)
if enemy1 == "championfly":
  draw (-375, 200, 12.5, champflyall)
  '''pixelsize = 12.5
  t.goto(-375, 200)
  gotoy = 187.5
  for color in champfly:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly2:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly3:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly4:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly5:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly6:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly7:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly8:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly9:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly10:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly11:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly12:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly13:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly14:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly15:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly16:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly17:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= pixelsize
  t.pendown()
  for color in champfly18:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  turtle.update()'''
  
  #fly printing code
turtle.tracer(0,0)
if enemy1 == "fly":
  draw(-375, 200, 20, flyall)
  '''
  pixelsize = 20
  t.goto(-375, 200)
  gotoy = 180
  for color in fly:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly2:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly3:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly4:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly5:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly6:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly7:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly8:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly9:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly10:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly11:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
  t.penup()
  
  t.goto(-375, gotoy)
  gotoy -= 20
  t.pendown()
  for color in fly12:
    t.color(color)
    t.begin_fill()
    for i in range (4):
      t.forward(pixelsize)
      t.right(90)
    t.end_fill()
    t.forward(pixelsize)
    t.penup()
    turtle.update()
    '''
