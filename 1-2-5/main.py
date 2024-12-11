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

# Setup Turtle
wn.screensize(900, 900)
wn.bgcolor('black')
player1.pencolor('white')
player2.pencolor('white')
player1_score.pencolor('white')
player2_score.pencolor('white')
game_wall.pencolor('white')
ball.pencolor('white')







# loop to keep window open
wn.listen()
wn.mainloop()