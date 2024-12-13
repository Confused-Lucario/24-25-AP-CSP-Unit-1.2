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
ball_size = 10
ball_speed = 2
game_wall_pen_size = 5

# Setup Turtle
wn.screensize(game_width + 200, game_height + 200)
wn.bgcolor('black')
player1.pencolor('white')
player2.pencolor('white')
player1_score.pencolor('white')
player2_score.pencolor('white')
game_wall.pencolor('white')
game_wall.speed('fastest')
game_wall.pensize(game_wall_pen_size)
game_wall.hideturtle()
ball.pencolor('white')
ball.speed(0)
ball.penup()
ball.shape('circle')
ball.turtlesize(ball_size/10)

# define functions
    # draws the boarder of the game, does not affect the bouncing code directly but the variables used do
def draw_game_boarder():
    game_wall.penup()
    game_wall.goto(game_width/2, game_height/2)
    game_wall.pendown()
    game_wall.goto(game_width/2, game_height/-2)
    game_wall.goto(game_width/-2, game_height/-2)
    game_wall.goto(game_width/-2, game_height/2)
    game_wall.goto(game_width/2, game_height/2)

    # launches the ball in a random direction, excluding 0/360,90,180,270 to avoid ball bouncing straight constantly
def launch_ball():
    # angle = rd.randint(0, 360)
    angle = 0
    while angle == 0 or angle == 90 or angle == 180 or angle == 270:
        angle = rd.randint(0, 360)
    ball.right(angle)


    # calculates the angle the ball needs to turn to bounce correctly along the y-axis (law of reflection)
def ball_bounce_y():
    if 0 < ball.heading() < 90:
        ball.right(ball.heading() * 2)
    elif 90 < ball.heading() < 180:
        ball.left((180-ball.heading()) * 2)
    elif 180 < ball.heading() < 270:
        ball.right((ball.heading() - 180) * 2)
    elif 270 < ball.heading() < 360:
        ball.left(360 - (ball.heading()) * 2)
    ball.forward(ball_speed)

    # calculates the angle the ball needs to turn to bounce correctly along the x-axis (law of reflection)
def ball_bounce_x():
    if 0 < ball.heading() < 90:
        ball.left((90 - ball.heading()) * 2)
    elif 90 < ball.heading() < 180:
        ball.right((ball.heading() - 90) * 2)
    elif 180 < ball.heading() < 270:
        ball.left(180 - (ball.heading()) * 2)
    elif 270 < ball.heading() < 360:
        ball.right((ball.heading() - 270) * 2)
    ball.forward(ball_speed)


# game code
draw_game_boarder()
launch_ball()

while True:
    # listens for keyboard input
    wn.listen()

    # checks if the ball is close to the wall on the y axis
    if ball.ycor() + ball_size + game_wall_pen_size >= game_height/2 or ball.ycor() - ball_size - game_wall_pen_size <= game_height/-2:
        ball_bounce_y()

    # checks if the ball is close to the wall on the x axis
    if ball.xcor() + ball_size + game_wall_pen_size >= game_width/2 or ball.xcor() - ball_size - game_wall_pen_size <= game_width/-2:
        ball_bounce_x()

    else:
        ball.forward(ball_speed)

# loop to keep window open

wn.mainloop()