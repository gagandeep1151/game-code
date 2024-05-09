#python turtle code 10 
#beautiful design in python
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.width(3)
t.speed(25)
col=('red','blue','pink','yellow','purple','green','orange','lime')
for i in range(500):
    t.pencolor(col[i%8])
    t.forward(i*4)
    t.right(200)
col=('red','blue','pink','yellow','purple','green','orange','lime')
for i in range(500):
    t.pencolor(col[i%8])
    t.forward(i*4)
    t.right(200)
col=('red','blue','pink','yellow','purple','green','orange','lime')
for i in range(500):
    t.pencolor(col[i%8])
    t.forward(i*4)
    t.right(200)