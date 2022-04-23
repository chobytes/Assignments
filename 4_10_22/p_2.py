import turtle as t
import math

#basic settings
t.pensize(1) 
t.speed("fastest")

t.up()

# draw the sin function
t.color("blue")
for x in range(-175,176):
    t.goto(x,50*math.sin((x/100)*2*math.pi))
    if not t.isdown():
        t.down()
t.up()

# draw the cos function
t.color("red")
for x in range(-175,176):
    t.goto(x,50*math.cos((x/100)*2*math.pi))
    if not t.isdown():
        t.down()
t.up()

#draw the x axis
t.color("black")
t.goto(-200,0)
t.down()
t.forward(400)
t.right(150)
t.forward(20)
t.up()
t.goto(200,0)
t.down()
t.right(60)
t.forward(20)
t.up()
t.home()

#draw the y axis
t.goto(0,-75)
t.right(270)
t.down()
t.forward(150)
t.right(150)
t.forward(20)
t.up()
t.goto(0,75)
t.right(60)
t.down()
t.forward(20)
t.up()
t.home()

#write the x-coordinates
t.goto(-100,-20)
t.write("-2\u03c0")
t.goto(100,-20)
t.write("2\u03c0")

#hide the pointer
t.hideturtle()


t.done()
