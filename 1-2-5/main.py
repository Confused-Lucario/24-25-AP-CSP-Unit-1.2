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
import time as tm


# explain the game ask for player 1 and player 2 names
print("Welcome to Pong, by Philip Birkland and Brandon Howland")
tm.sleep(2)
print("The controls for player 1 are (W Key) and (S Key)" + "\n" + "The controls for player 2 are (Arrow Key Up) and (Arrow Key Down)")
tm.sleep(3)
print("every bounce on your player speeds up the ball")
print("to win the game one side has to score 5 points")
tm.sleep(3)
player1_name = input("Please enter player 1 (left) name: ")
player2_name = input("Please enter player 2 (right) name: ")
print("the game will appear in 5 seconds, click on the window that opens")
tm.sleep(5)

# Initialize Variables
wn = trtl.Screen()
    # moves window to top of screen after screen initializes and focuses screen
root_window = wn.getcanvas().winfo_toplevel()
root_window.call('wm', 'attributes', '.', '-topmost', '1')
root_window.call('wm', 'attributes', '.', '-topmost', '0')
tm.sleep(2)
wn.update()
game_wall = trtl.Turtle()
player1 = trtl.Turtle()
player2 = trtl.Turtle()
ball = trtl.Turtle()
player1_score = trtl.Turtle()
player2_score = trtl.Turtle()
    # changes the play area size
game_width = 700
game_height = 400
    # changes the ball size and speed
ball_size = 10
ball_speed = 3
    # changes the thickness of the walls
game_wall_pen_size = 5
    # changes the size of the player bars and the amount they move
player_width = 20
player_speed = 6
    # font setup
text_font = ("Arial", 20, "normal")
    # list of player's scores and amount needed to score to win
scores = [0,0]
win_score = 5

# Setup Turtle parameters
wn.screensize(game_width + 200, game_height + 200)
wn.bgcolor('black')
    # player 1 setup code
player1.color('blue')
player1.shape('square')
player1.turtlesize(player_width/10, .5)
player1.penup()
player1.goto(game_width/-2 + game_wall_pen_size + 3,0)
    # player 2 setup code
player2.color('red')
player2.shape('square')
player2.turtlesize(player_width/10, .5)
player2.penup()
player2.goto(game_width/2 - game_wall_pen_size - 3,0)
    # player 1 and 2 score setup
player1_score.pencolor('blue')
player1_score.penup()
player1_score.goto(game_width/-2 - 50, game_height/2 + 50)
player1_score.hideturtle()
player1_score.write(str(player1_name) + ": " + str(scores[0]), align='center', font=text_font)
player2_score.pencolor('red')
player2_score.penup()
player2_score.goto(game_width/2 + 50, game_height/2 + 50)
player2_score.hideturtle()
player2_score.write(str(player2_name) + ": " + str(scores[1]), align='center', font=text_font)
    # game wall setup
game_wall.pencolor('white')
game_wall.speed('fastest')
game_wall.pensize(game_wall_pen_size)
game_wall.hideturtle()
    # ball setup
ball.hideturtle()
ball.pencolor('white')
ball.speed(0)
ball.penup()
ball.shape('circle')
ball.turtlesize(ball_size/10)

# key state tracking
key_states = {"w": False, "s": False, "Up": False, "Down": False}

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

    # starts the game by counting down from 3, then choosing the random angle the ball will launch at
def start_game():
    ball.hideturtle()
    ball.goto(0,0)
    player1.goto(game_width/-2 + game_wall_pen_size + 3,0)
    player2.goto(game_width / 2 - game_wall_pen_size - 3, 0)
    ball.write("3", align="center", font=text_font)
    tm.sleep(1)
    wn.update()
    ball.clear()
    ball.write("2", align="center", font=text_font)
    tm.sleep(1)
    wn.update()
    ball.clear()
    ball.write("1", align="center", font=text_font)
    tm.sleep(1)
    wn.update()
    ball.clear()
    ball.showturtle()
    ball.setheading(0)
    angle = rd.randint(0, 360)
    while 345<=angle<=15 or 75<=angle<=105 or 165<=angle<=195 or 255<=angle<=285:
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

    # player 1 movement functions
def player1_up():
    player1.goto(player1.xcor(), player1.ycor() + player_speed)
def player1_down():
    player1.goto(player1.xcor(), player1.ycor() - player_speed)

    # player 2 movement functions
def player2_up():
    player2.goto(player2.xcor(), player2.ycor() + player_speed)
def player2_down():
    player2.goto(player2.xcor(), player2.ycor() - player_speed)

    # function to update key states
def key_press(key):
    key_states[key] = True
def key_release(key):
    key_states[key] = False

# function that increments scores, checks if someone won, and resets play field
def goal_scored():
    global ball_speed
    global scores
    if ball.xcor()>0:
        scores[0] += 1
    elif ball.xcor()<0:
        scores[1] += 1
    player1_score.clear()
    player1_score.write(str(player1_name) + ": " + str(scores[0]), align='center', font=text_font)
    player2_score.clear()
    player2_score.write(str(player2_name) + ": " + str(scores[1]), align='center', font=text_font)
    ball_speed = 2
    if scores[0] == win_score:
        ball.hideturtle()
        ball.goto(0,0)
        ball.write(str(player2_name) + " wins!", align="center", font=text_font)
        wn.update()
        tm.sleep(5)
        wn.bye()
    if scores[1] == win_score:
        ball.hideturtle()
        ball.goto(0,0)
        ball.write(str(player2_name) + " wins!", align="center", font=text_font)
        wn.update()
        tm.sleep(5)
        wn.bye()
    wn.update()
    start_game()
    tm.sleep(1)
    main_loop()




# controls
    # makes the screen wait for input
wn.listen()
    # player 1's controls
wn.onkeypress(lambda: key_press("w"),"w")
wn.onkeyrelease(lambda: key_release("w"), "w")
wn.onkeypress(lambda: key_press("s"),"s")
wn.onkeyrelease(lambda: key_release("s"), "s")
    # player 2's controls
wn.onkeypress(lambda: key_press("Up"),"Up")
wn.onkeyrelease(lambda: key_release("Up"),"Up")
wn.onkeypress(lambda: key_press("Down"),"Down")
wn.onkeyrelease(lambda: key_release("Down"),"Down")


# main loop, the main loop is a looping function to keep everything at the same fps (16 ms is around 60 fps)
def main_loop():
    global ball_speed
    # moving player 1
    if key_states["w"] and player1.ycor() < game_height/2 - player_width:
        player1_up()
    if key_states["s"] and player1.ycor() > game_height/-2 + player_width:
        player1_down()
    # moving player 2
    if key_states["Up"] and player2.ycor() < game_height/2 - player_width:
        player2_up()
    if key_states["Down"] and player2.ycor() > game_height/-2 + player_width:
        player2_down()

    # checks if the ball is close to the wall on the y-axis
    if ball.ycor() + ball_size + game_wall_pen_size >= game_height/2 or ball.ycor() - ball_size - game_wall_pen_size <= game_height/-2:
        ball_bounce_y()
    else:
        ball.forward(ball_speed)
    # checks if the ball is close to the wall on player1 side
    if ball.xcor() + ball_size + game_wall_pen_size + 10 >= game_width/2 or ball.xcor() - ball_size - game_wall_pen_size - 10 <= game_width/-2:
        # checks if the ball and player are aligned to bounce, and which side the ball is on
        if (player1.ycor() + player_width) > ball.ycor() > (player1.ycor() - player_width) and ball.xcor() < 0:
            ball_bounce_x()
            ball_speed += 1
        elif (player2.ycor() + player_width) > ball.ycor() > (player2.ycor() - player_width) and ball.xcor() > 0:
            ball_bounce_x()
            ball_speed += 1
    if ball.xcor() + ball_size + game_wall_pen_size >= game_width / 2 or ball.xcor() - ball_size - game_wall_pen_size <= game_width / -2:
        goal_scored()
        return
    # updates the turtles and loops again at ~60 fps
    wn.update()
    wn.ontimer(main_loop, 16)

# game code start
wn.tracer(0)
draw_game_boarder()
wn.update()
start_game()
tm.sleep(1)
main_loop()

wn.mainloop()