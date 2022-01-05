from turtle import * 
import random 
paletteMaker = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'] 
color = [] 
while len(color) < 24: 
    if (col := ''.join(['#', *random.choices(paletteMaker, k = 6)])) not in color: 
        color.append(col) 
print(color) 
t = Turtle() 
t.speed(10) 
t.pensize(2) 
l = 50 
t.pu() 
t.goto(-l,l/2) 
t.pd() 
theta = 30 
t.lt(30) 
for i in range(6): 
    for j in range(5): 
        t.rt(30) 
        t.color(color[random.randint(0,23)], color[random.randint(0,23)]) 
        t.begin_fill() 
        t.fd(l) 
        if j == 0: 
            x, y, head = *t.position(), t.heading() 
        t.lt(theta) 
        t.fd(l) 
        t.lt(180 - theta) 
        t.fd(l) 
        t.lt(theta) 
        t.fd(l) 
        t.end_fill() 
        t.lt(180 - theta) 
        t.fd(l) 
        theta += 30 
        print(theta) 
    t.pu() 
    t.goto(x, y) 
    t.pd() 
    t.seth(head - 30) 
    theta = 30 
