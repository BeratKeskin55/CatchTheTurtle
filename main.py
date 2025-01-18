import turtle
import time
import random

Font = ("arial",35,"normal")

screen = turtle.Screen()
turtle.bgcolor("black")
text_turtle = turtle.Turtle()
turtle_turtle = turtle.Turtle()
counter_runing = True
point_turtle = turtle.Turtle()
point = 0
circle_pos = (0,0)
turtles =[text_turtle,turtle_turtle,point_turtle]

for color in turtles:
    color.color("white")
    color.hideturtle()

def update_point_display():
    point_turtle.clear()
    point_turtle.write(f"point:{point}",align='center',font=Font)

def countdown(time):
    global counter_runing
    screen.onclick(None)
    text_turtle.clear()

    if time > 0 :
        text_turtle.penup()
        text_turtle.goto(0, 300)
        text_turtle.pendown()
        text_turtle.write(time,align='center',font=Font)
        turtle.ontimer(lambda :countdown(time-1),1000)
    else:
        text_turtle.penup()
        text_turtle.goto(0,300)
        text_turtle.pendown()
        text_turtle.write("click screen",align='center',font=Font)
        screen.onclick(click_screen)
        counter_runing = False

turtle_instance = turtle.Turtle()
turtle_instance.color("#77B254")
def circle():
    global counter_runing
    turtle_instance.clear()
    if counter_runing:
        turtle_instance.penup()
        x,y = random.randint(-300, 150),random.randint(100,150)
        turtle_instance.goto(x,y)
        turtle_instance.pendown()
        turtle_instance.speed(0)
        turtle_instance.shape("turtle")
        turtle_instance.shapesize(2.5)
        screen.ontimer(circle,500)

def screen_ontimer(x,y):
   global point
   if turtle_instance.distance(x,y) < 70:
        point+=1
        update_point_display()

def drawing_board_ontimer(x,y):
    global counter_runing
    counter_runing=True
    screen.onclick(None)
    countdown(30)
    circle()

def puan_tikla():
    global point
    point+=1
    update_point_display()

def click_screen(x,y):
    drawing_board_ontimer(x,y)
    screen_ontimer(x,y)
    puan_tikla()

def point_screen():
    point_turtle.penup()
    point_turtle.goto(0, 240)
    point_turtle.pendown()
    point_turtle.speed(0)
    update_point_display()

point_screen()
turtle_instance.speed(0)
screen.onclick(click_screen)
text_turtle.penup()
text_turtle.goto(0,300)
text_turtle.pendown()
text_turtle.write("Click screen",align="center",font=Font)
turtle.done()
