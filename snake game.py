
import turtle  
import time 
import random

delay = 0.1

score = 0 
high_score = 0

sn = turtle.Screen()
sn.title("snake game")
sn.bgcolor("green")
sn.setup(width = 600,height = 600) 
sn.tracer(0)  

#snake head 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segment = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score=0  High score = 0",align = "center",font = ("courier",24,"normal"))


#functions moves in keyboard
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

#functions moes in direction

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20) 

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20) 

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20) 

sn.listen()
sn.onkeypress(go_up,"w")
sn.onkeypress(go_down,"s")
sn.onkeypress(go_left,"a")
sn.onkeypress(go_right,"d")

while True:
    sn.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()<-290 or head.ycor()>290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
  

        for segments in segment:
            segments.goto(1000,1000)

        segment.clear() 

    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,250)
        food.goto(x,y)

        #add a segment 
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segment.append(new_segment)


        score += 10
        
        if score>high_score:
            high_score = score
        pen.clear()
        pen.write("score : {} high score: {}".format(score,high_score),align="center",font = ("courier",24,"normal"))
    
    for index in range(len(segment)-1, 0 ,-1):
        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x,y)
    
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)


    move()

    for segments in segment:
        if segments.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.distance = "stop"

            for segments in segment:
                segments.goto(1000,1000)

            segment.clear()


    time.sleep(delay) 
    
sn.mainloop()
