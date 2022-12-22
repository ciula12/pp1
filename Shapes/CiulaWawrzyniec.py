from turtle import *
import turtle as t
import random 
import time

start_time = time.time()
t.title("Wawrzyniec Ciuła")
screen = t.Screen()
screen.colormode(255)
t.Screen().cv._rootwindow.state("zoomed")
screen.bgcolor(51, 102, 204)
t.speed(50)

#SQUARE
#x,y -> starting coordinations
#size -> side length
def square(x,y,width,line_color,bg_color,angle,size):
    pensize(width)
    color(line_color,bg_color)
    setheading(angle)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    heading()
    for x in range (4):
        forward(size)
        left(90)
    end_fill()

#STAR
#x,y -> starting coordinations
#size -> first line length
def star(x,y,width,line_color,bg_color,angle,size):
    pensize(width)
    color(line_color,bg_color)
    setheading(angle)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    heading()
    for x in range (5):
        forward(size*0.3825)
        penup()
        forward(size*0.235)
        pendown()
        forward(size*0.3825)
        left(144)
    end_fill()

#RIGHT TRIANGLE
#x,y -> starting coordinations
def rightT(x,y,width,line_color,bg_color,angle,side_a,side_b):
    pensize(width)
    color(line_color,bg_color)
    setheading(angle)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    heading()

    forward(side_a)
    left(90)
    forward(side_b)
    goto(x,y)

    end_fill()

#ARROW
#x,y -> pointing coordinations
#arrow_size -> size of the pointing part
def arrow(x,y,width,line_color,bg_color,angle,length,arrow_size):
    pensize(width)
    color(line_color,bg_color)
    setheading(angle)
    arrow_side = (arrow_size*0.7072/3*2)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    heading()

    left(135)
    forward(arrow_size)
    left(135)
    forward(arrow_side)
    right(90)
    forward(length)
    left(90)
    forward(arrow_side)
    left(90)
    forward(length)
    right(90)
    forward(arrow_side)
    goto(x,y)

    end_fill()

#RING
#x,y -> middle coordinations
def ring(x,y,width,line_color_first,bg_color_first,first_radius,line_color_sec,bg_color_sec,second_radius):
    pensize(width)
    setheading(0)
    heading()
    
    if first_radius >= second_radius:
        penup()

        color(line_color_first,bg_color_first)
        goto(x,(y-first_radius))
        pendown()
        begin_fill()
        circle(first_radius)
        end_fill()
        penup()

        color(line_color_sec,bg_color_sec)
        goto(x,(y-second_radius))
        pendown()
        begin_fill()
        circle(second_radius)
        end_fill()
    else:
        penup()

        color(line_color_sec,bg_color_sec)
        goto(x,(y-second_radius))
        pendown()
        begin_fill()
        circle(second_radius)
        end_fill()
        penup()

        color(line_color_first,bg_color_first)
        goto(x,(y-first_radius))
        pendown()
        begin_fill()
        circle(first_radius)
        end_fill()

def info():
    penup()
    color("black")
    goto(730,480)
    pensize(2)
    setheading(0)
    heading()
    #name
    #W
    pendown()
    right(90)
    forward(15)
    left(135)
    forward(10)
    right(90)
    forward(10)
    right(-135)
    forward(15)
    penup()
    #A
    Ax=750
    Ay=465
    goto(Ax,Ay)
    setheading(0)
    heading()
    pendown()
    goto(Ax+6,Ay+15)
    goto(Ax+12,Ay)
    penup()
    goto(Ax+4,Ay+6)
    pendown()
    goto(Ax+9,Ay+6)
    penup()
    #W
    goto(767,480)
    setheading(0)
    heading()
    pendown()
    right(90)
    forward(15)
    left(135)
    forward(10)
    right(90)
    forward(10)
    right(-135)
    forward(15)
    penup()
    #R
    goto(787,480)
    setheading(0)
    heading()
    pendown()
    right(90)
    forward(15)
    back(15)
    left(90)
    forward(5)
    right(45)
    forward(5)
    right(90)
    forward(5)
    right(45)
    forward(5)
    left(135)
    forward(13)
    penup()
    #Z
    goto(800,480)
    setheading(0)
    heading()
    pendown()
    forward(9)
    right(120)
    forward(17)
    left(120)
    forward(10)
    penup()
    #Y
    goto(813,480)
    setheading(-60)
    heading()
    pendown()
    forward(10)
    left(120)
    forward(10)
    back(10)
    left(210)
    forward(7)
    penup()
    #N
    goto(828,480)
    setheading(-90)
    heading()
    pendown()
    forward(15)
    back(16)
    left(30)
    forward(18)
    left(150)
    forward(15)
    penup()
    #I
    goto(843,480)
    setheading(-90)
    heading()
    pendown()
    forward(15)
    penup()
    #E
    Ex=848
    Ey=480
    goto(Ex,Ey)
    pendown()
    goto(Ex+6,Ey)
    penup()
    goto(Ex,Ey)
    pendown()
    goto(Ex,Ey-7)
    goto(Ex+5,Ey-7)
    penup()
    goto(Ex,Ey-7)
    pendown()
    goto(Ex,Ey-15)
    goto(Ex+6,Ey-15)
    penup()
    #C
    Ex=865
    Ey=480
    goto(Ex,Ey)
    setheading(180)
    heading()
    pendown()
    circle(7.5,-30)
    penup()
    circle(7.5,30)
    pendown()
    circle(7.5,230)
    penup()

    #surname
    #C
    Ex=735
    Ey=450
    goto(Ex,Ey)
    setheading(180)
    heading()
    pendown()
    circle(7.5,-30)
    penup()
    circle(7.5,30)
    pendown()
    circle(7.5,230)
    penup()
    #I
    goto(746,450)
    setheading(-90)
    heading()
    pendown()
    forward(15)
    penup()    
    #U
    goto(750,450)
    setheading(-90)
    heading()
    pendown()
    forward(10)
    circle(5,180)
    forward(10)
    penup()  
    #Ł
    goto(765,450)
    setheading(-90)
    heading()
    pendown()
    forward(15)
    left(90)
    forward(8)
    back(8)
    left(90)
    forward(7.5)
    right(60)
    forward(7)
    penup()  
    #A
    Ax=777
    Ay=450-15
    goto(Ax,Ay)
    setheading(0)
    heading()
    pendown()
    goto(Ax+6,Ay+15)
    goto(Ax+12,Ay)
    penup()
    goto(Ax+4,Ay+6)
    pendown()
    goto(Ax+9,Ay+6)
    penup()
    #group number
    #Z
    goto(730,420)
    setheading(0)
    heading()
    pendown()
    forward(9)
    right(120)
    forward(17)
    left(120)
    forward(10)
    penup()
    #Z
    goto(743,420)
    setheading(0)
    heading()
    pendown()
    forward(9)
    right(120)
    forward(17)
    left(120)
    forward(10)
    penup() 
    #I
    goto(758,420)
    setheading(-90)
    heading()
    pendown()
    forward(15)
    penup()    
    #S
    goto(757,420)
    setheading(0)
    heading()
    penup()
    forward(10)
    pendown()   
    left(180)
    circle(7.5/2,-45)
    circle(7.5/2,225)
    left(180)
    circle(7.5/2,-250)
    penup()
    #S
    goto(768,420)
    setheading(0)
    heading()
    penup()
    forward(10)
    pendown()   
    left(180)
    circle(7.5/2,-45)
    circle(7.5/2,225)
    left(180)
    circle(7.5/2,-250)
    penup()
    
    #1  
    goto(785,420)
    setheading(-90)
    heading()
    forward(6)
    left(150)
    pendown()
    forward(7)
    right(150)
    forward(15)
    penup()  
    #- 
    goto(793,420)
    setheading(-90)
    heading()
    forward(7.5)
    left(90)
    pendown()
    forward(7)
    penup()  
    #1 X4 
    for hh in range(4):
        firstX = 802+(hh*10)
        YY = 420
        goto(firstX,YY)
        setheading(-90)
        heading()
        forward(6)
        left(150)
        pendown()
        forward(7)
        right(150)
        forward(15)
        penup()  

def random_color():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        


#MAIN

screen.tracer(True)

#STARS
for oo in range(-900,656,random.randint(110,130)): 
    star(oo,random.randint(270, 500),random.randint(2, 3),random_color(),'yellow',random.randint(-360,360),random.randint(35,52))
                                                                                                              
#HOUSES
for oo in range(-900,900,random.randint(130,170)): 
    Yran = random.randint(-500, -200)
    sqsize = random.randint(50,80)
    winsize = random.randint(int(sqsize/4),int(sqsize/3))
    square(oo, Yran, 3, 'saddlebrown',random_color(), 0, sqsize)
    rightT(oo-sqsize/2, Yran-1, 1, 'black','black', 0, sqsize*2, 0)
    rightT(oo-sqsize/4, Yran-2, 1, 'black','black', 0, sqsize*1.5, 0)
    rightT((oo+(sqsize*1.2)), (Yran+sqsize), 3, 'saddlebrown',random_color(), 135, sqsize, sqsize)
    ring((oo+(sqsize*0.5)), (Yran+(sqsize*0.5)), 2, 'saddlebrown',random_color(), winsize, 'saddlebrown','lightblue', random.randint(int(winsize/2),int(winsize/1.5)))

#TREES
for oo in range(-900,900,random.randint(110,130)): 
    Yran = random.randint(-70, 150)
    Aangle = random.randint(86, 94)
    l = random.randint(7,14) 
    sizearrow= random.randint(l*3,l*4)
    for tt in range(3):
        arrow(oo, Yran+tt*l, 1, (0, 102, 0),(0, 102, 0), Aangle, l, sizearrow-(tt*2.5))

#NAME,SURNAME,GROUP
info()

#ADDITIONAL_ARROWS
for oo in range(720,900,51):
    if oo%2==1:
        change=-7
        col=(255, 50, 150)
    else: 
        change=7
        col=(180, 0, 0)
    arrow(oo, 380+change, 3, "black", col, 90, 40, 30)

penup()
home()
screen.tracer(False)

for x in range(8):
    print("")
print(f"Seconds: {(time.time() - start_time)}")


screen.exitonclick()