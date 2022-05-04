import turtle as t
from math import cos,sin,pi

spin_angle = 0

def fan_update():

    global spin_angle

    #Clear the screen
    t.clear() 
    t.begin_fill()

    #A four-step loop to draw the fan blades seperately
    for angle_s,angle_e in [(x*90 + spin_angle, x*90 + 30 + spin_angle) for x in [0,1,2,3]]:
        #Straight edge 1
        t.forward(100)
        #Curved edge
        for d in range(angle_s,angle_e):
            t.goto(100*cos(d/360*2*pi),100*sin(d/360*2*pi))
        #Straight edge 2
        t.goto(0,0)
        t.setheading(angle_e + 60)

    t.end_fill()
    spin_angle = spin_angle + 1 if spin_angle != 360 else 0 

    #Upadate the screen every 10ms, delete this sentence if a static image is required to display
    screen.ontimer(fan_update, 10)

t.tracer(0,0)
screen = t.Screen()
screen.setup(width = 300,height = 300)

fan_update()
screen.mainloop()




        
