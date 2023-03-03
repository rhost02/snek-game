#diff between tracer and speed
import turtle
import time
import random

score = 0
high_score = 0
delay = 0.1

window = turtle.Screen()
window.title("snek by @snolink")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.pu()
snake.goto(0, 0)
snake.direction = "stop"

cherry = turtle.Turtle()
cherry.speed(0)
cherry.shape("square")
cherry.color("red")
cherry.pu()
cherry.goto(0, 100)

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("cyan")
scoreboard.pu()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Score: 0      High Score: 0", align="center", font=("courier", 24, "normal"))

def go_up():
    if snake.direction != "down":
        snake.direction = "up"
        
def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"
        
def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")

segments = []

while True:
    window.update()
    #collision with boarder
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"
        
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        
        score = 0
        delay = 0.1
        
        scoreboard.clear()
        scoreboard.write(f"Score: {score}      High Score: {high_score}", align="center", font=("courier", 24, "normal"))
    
    if snake.distance(cherry) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        cherry.goto(x, y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.pu()
        segments.append(new_segment)
        
        delay -= 0.001
        score += 10
        
        if score > high_score:
            high_score = score
        scoreboard.clear()
        scoreboard.write(f"Score: {score}      High Score: {high_score}", align="center", font=("courier", 24, "normal"))

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    
    if len(segments) > 0:
        segments[0].goto(snake.xcor(), snake.ycor())
    move()
    
    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            scoreboard.clear()
            scoreboard.write(f"Score: {score}      High Score: {high_score}", align="center", font=("courier", 24, "normal"))
    time.sleep(delay)
    
window.mainloop()