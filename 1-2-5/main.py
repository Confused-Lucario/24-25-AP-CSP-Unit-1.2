##############################################################################
#   main.py.
#   Idea behind the code:
#       make a boarder, 2 players, a ball, and a score
#       make functions for ball bouncing on each axis and for scoring
#       set up player controls
#       when a ball scores, add 1 to the score and reset playing field
#       store scores in list for high scores
##############################################################################
import turtle as trtl
import random as rd

# Initialize Variables
wn = trtl.Screen()
game_wall = trtl.Turtle()
player1 = trtl.Turtle()
player2 = trtl.Turtle()
ball = trtl.Turtle()
player1_score = trtl.Turtle()
player2_score = trtl.Turtle()

# game parameters
game_width = 700
game_height = 400
ball_size = 50

# Setup Turtle
wn.screensize(game_width + 200, game_height + 200)
wn.bgcolor('black')
player1.pencolor('white')
player2.pencolor('white')
player1_score.pencolor('white')
player2_score.pencolor('white')
game_wall.pencolor('white')
game_wall.speed('fastest')
game_wall.pensize(5)
game_wall.hideturtle()
ball.pencolor('white')
ball.speed(1)
ball.penup()

# define functions
def draw_game_boarder():
    game_wall.penup()
    game_wall.goto(game_width/2, game_height/2)
    game_wall.pendown()
    game_wall.goto(game_width/2, game_height/-2)
    game_wall.goto(game_width/-2, game_height/-2)
    game_wall.goto(game_width/-2, game_height/2)
    game_wall.goto(game_width/2, game_height/2)

def launch_ball():
    ball.setheading(rd.randint(0, 360))



def ball_bounce_y():
    if ball.heading() > 0 and ball.heading() < 90:
        ball.setheading(ball.heading() - 90)
        ball.forward(ball_size)
    elif ball.heading() > 90 and ball.heading() < 180:
        ball.setheading(ball.heading() + 90)
        ball.forward(ball_size)
    elif ball.heading() > 180 and ball.heading() < 270:
        ball.setheading(ball.heading() - 90)
        ball.forward(ball_size)
    elif ball.heading() > 270 and ball.heading() < 360:
        ball.setheading(ball.heading() + 90)
        ball.forward(ball_size)

def ball_bounce_x():
    if ball.heading() > 0 and ball.heading() < 90:
        ball.setheading(ball.heading() + 90)
        ball.forward(ball_size)
    elif ball.heading() > 90 and ball.heading() < 180:
        ball.setheading(ball.heading() - 90)
        ball.forward(ball_size)
    elif ball.heading() > 180 and ball.heading() < 270:
        ball.setheading(ball.heading() + 90)
        ball.forward(ball_size)
    elif ball.heading() > 270 and ball.heading() < 360:
        ball.setheading(ball.heading() - 90)
        ball.forward(ball_size)


# game code
draw_game_boarder()

launch_ball()

while True:
    if ball.ycor() + 50 > game_height/2 or ball.ycor() - 50 < game_height/-2:
        ball_bounce_y()

    if ball.xcor() + 50 > game_width/2 or ball.xcor() - 50 < game_width/-2:
        ball_bounce_x()

    else:
        ball.forward(10)

# loop to keep window open
wn.listen()
wn.mainloop()