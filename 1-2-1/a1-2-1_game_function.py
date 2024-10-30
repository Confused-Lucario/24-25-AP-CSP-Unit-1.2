# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"

score = 0

font_setup = ("Arial", 20, "normal")

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
spot = t.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)
spot.speed(0)

score_writer = t.Turtle()

counter =  t.Turtle()

#-----game functions--------

def spot_clicked(x,y):
    global timer_up
    if timer_up == False:
        update_score()
        change_position()
    else:
        spot.hideturtle()

def change_position():
    newx = rand.randint(-400,400)
    newy = rand.randint(-300,300)
    spot.penup()
    spot.hideturtle()
    spot.goto(newx, newy)
    spot.pendown()
    spot.showturtle()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0,0)
score_writer.pendown()

counter.hideturtle()
counter.penup()
counter.goto(-450,350)
counter.pendown()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
spot.onclick(spot_clicked)
wn = t.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()
