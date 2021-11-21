#Snake
#Make a turtle that moves up/down/right/left by pressing arrow keys
#Make food randomly appear on screen

import turtle
import random
import math
import time

## Make board
wn = turtle.Screen()
wn.tracer(0)
wn.bgcolor("black")
wn.setup(width=640, height=640)
wn.title("Snakes")

## Make border

borderpen = turtle.Turtle()
borderpen.color('white')
borderpen.penup()
borderpen.speed(0)
borderpen.setpos(-300, -300)
borderpen.pensize(8)
borderpen.setheading(90)
borderpen.pendown()
for side in range(4):
    borderpen.fd(600)
    borderpen.right(90)
borderpen.penup()
borderpen.hideturtle()

## Show score
score = 0
highscore = 0
score_pen = turtle.Turtle()
score_pen.pensize(4)
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setpos(-270, 270)
score_pen.pendown()
score_pen.write(f"Score: {score}      High score: {highscore}")
score_pen.penup()
score_pen.hideturtle()


## Make player snake
player_snake = turtle.Turtle()
player_snake.penup()
player_snake.setpos(0, 0)
player_snake.color("white")
player_snake.shape("square")
player_snake_speed_x = 0
player_snake_speed_y = 0

## Addons to player_snake
addons = []
def snake_addon():
    addon = turtle.Turtle()
    addon.hideturtle()
    addon.penup()
    addon.setpos(0, 0)
    addon.color("white")
    addon.shape("turtle")
    addon.setposition(player_snake.xcor(), player_snake.ycor())
    addon.showturtle()
    addons.append(addon)
    


## Make player_snake able to move
    ## LEFT/RIGHT
def move_left():
    global player_snake_speed_x
    global player_snake_speed_y
    global dif
    player_snake_speed_y = 0
    player_snake_speed_x = -2 - dif
    player_snake.setheading(180)

def move_right():
    global player_snake_speed_x
    global player_snake_speed_y
    global dif
    player_snake_speed_y = 0
    player_snake_speed_x = 2 + dif
    player_snake.setheading(0)

def move_left_or_right():
    global player_snake_speed_x
    x = player_snake.xcor()
    x += player_snake_speed_x
    player_snake.setx(x)

## UP/RIGHT
def move_up():
    global player_snake_speed_y
    global player_snake_speed_x
    global dif
    player_snake_speed_x = 0
    player_snake_speed_y = 2 + dif
    player_snake.setheading(90)
    
def move_down():
    global player_snake_speed_y
    global player_snake_speed_x
    global dif
    player_snake_speed_x = 0 
    player_snake_speed_y = -2 - dif
    player_snake.setheading(270)

def move_down_or_up():
    global player_snake_speed_y
    y = player_snake.ycor()
    y += player_snake_speed_y
    player_snake.sety(y)
      
## Assign keyboard keys to movement of player
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")

## Make apples appear randomly on board
apples = turtle.Turtle()
apples.shape("circle")
apples.color("red")
apples.penup()
apples.shapesize(0.5, 0.5, 0.1)
apple_x = random.randint(-280, 280)
apple_y = random.randint(-280, 280)
apples.setpos(apple_x, apple_y)

## Check for collision between snake and apples
dif = 0
#def isCollision(t1, t2):
    #global dif
    #global score
    #distance = math.sqrt((player_snake.ycor() - apples.ycor())**2 + (player_snake.xcor() - apples.xcor())**2)
    #if distance < 20:
    #if player_snake.distance(apples) < 20:
      #  dif += 0.2
       # apples.hideturtle()
        #apples.setposition(random.randint(-280, 280), random.randint(-280, 280))
        #apples.showturtle()
        #score += 10
        #score_update(score)

        
        
        


## Make a function for score updating
def score_update(score):
    global highscore
    score_pen.setpos(-270, 270)
    score_pen.clear()
    score_pen.pendown()
    if score > highscore:
        highscore = score
    score_pen.write(f"Score: {score} High score: {highscore}")
    score_pen.penup()
    
    





## Main game loop

while True:
    wn.update()

    # check for collision between snake and apples
    if player_snake.distance(apples) < 20:
        dif += 0.5
        apples.hideturtle()
        apples.setposition(random.randint(-280, 280), random.randint(-280, 280))
        apples.showturtle()
        #increase score
        score += 10
        score_update(score)

        
        new_segment = turtle.Turtle()
        new_segment.hideturtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        addons.append(new_segment)
    # move segments to previous ones' places
    for index in range(len(addons)-1, 0, -1):
        xx = addons[index-1].xcor()
        yy = addons[index-1].ycor()
        addons[index].goto(xx, yy)
        new_segment.showturtle()

    # move segment[0] to the plac of the head
    if len(addons) > 0:
        x = player_snake.xcor()
        y = player_snake.ycor()
        addons[0].goto(x, y)
        
    move_left_or_right()
    x = player_snake.xcor()
    if x > 285 or x < -285:
        print("Game Over")
        break

    move_down_or_up()
    y = player_snake.ycor()
    if y > 290 or y < -290:
        print("Game Over")
        break

    time.sleep(0.015)
    
    
        
    ##isCollision(player_snake, apples)
        

    
