from turtle import *
import turtle as t
import random 


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
    goto(750,465)
    setheading(0)
    heading()
    pendown()
    goto(756,480)
    goto(762,465)
    penup()
    goto(754,471)
    pendown()
    goto(759,471)
    penup()
    #A
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
    #Z
    #Y
    #N
    #I
    #E
    #C

    #surname
    #C
    #I
    #U
    #Ł
    #A
    
    #group number
    

def random_color():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        

#MAIN



screen.tracer(True)


"""for oo in range(-900,700,random.randint(50,100)):
    star(oo,random.randint(270, 500),random.randint(2, 3),random_color(),'yellow',180,random.randint(40,60))


for oo in range(-900,900,random.randint(100,150)):
    Yran = random.randint(-540, -200)
    sqsize = random.randint(50,80)
    winsize = random.randint(int(sqsize/4),int(sqsize/3))
    square(oo, Yran, 3, 'saddlebrown',random_color(), 0, sqsize)
    rightT(oo-sqsize/2, Yran-1, 1, 'black','black', 0, sqsize*2, 0)
    rightT(oo-sqsize/4, Yran-2, 1, 'black','black', 0, sqsize*1.5, 0)
    rightT((oo+(sqsize*1.2)), (Yran+sqsize), 3, 'saddlebrown',random_color(), 135, sqsize, sqsize)
    ring((oo+(sqsize*0.5)), (Yran+(sqsize*0.5)), 2, 'saddlebrown',random_color(), winsize, 'saddlebrown','lightblue', random.randint(int(winsize/2),int(winsize/1.5)))"""

info()

penup()
home()

screen.exitonclick()
