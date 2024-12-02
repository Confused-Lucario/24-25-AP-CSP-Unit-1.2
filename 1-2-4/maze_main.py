import random as rn
import turtle as t

# variables
wn = t.Screen()
maze_wall = t.Turtle()
length = 20
inf = 1
maze_wall.speed(0)
maze_wall.color('black')
maze_wall.pensize(5)

# functions
def maze_wall_straight():
    maze_wall.pendown()
    maze_wall.forward(length)
    maze_wall.penup()

def maze_wall_door():
    maze_wall.penup()
    maze_wall.forward(length)

def maze_wall_block():
    maze_wall.pendown()
    maze_wall.left(90)
    maze_wall.forward(length*2)
    maze_wall.backward(length*2)
    maze_wall.right(90)
    maze_wall.forward(length)
    maze_wall.penup()

for wall in range(22):
    for walls in range(inf):
        random_wall = rn.randrange(0,3)
        if random_wall == 0:
            maze_wall_straight()
        elif random_wall == 1:
            maze_wall_door()
        elif random_wall == 2:
            maze_wall_block()
    inf += 1
    maze_wall.left(90)


wn.listen()
t.mainloop()