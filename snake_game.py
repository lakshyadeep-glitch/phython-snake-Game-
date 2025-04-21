import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

win = turtle.Screen()
win.title("Snake Game 🐍")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "bold"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

while True:
    win.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        death_message = turtle.Turtle()
        death_message.color("red")
        death_message.penup()
        death_message.hideturtle()
        death_message.goto(0, 0)
        death_message.write("💀 Your Snake is Dead!", align="center", font=("Courier", 20, "bold"))
        time.sleep(2)
        death_message.clear()

        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "bold"))

    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "bold"))

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            death_message = turtle.Turtle()
            death_message.color("red")
            death_message.penup()
            death_message.hideturtle()
            death_message.goto(0, 0)
            death_message.write("💀 Your Snake is Dead!", align="center", font=("Courier", 20, "bold"))
            time.sleep(2)
            death_message.clear()

            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            score_display.clear()
            score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "bold"))

    time.sleep(delay)
