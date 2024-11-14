#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
background_image = "background.gif"
font_setup = ("Arial", 74, "bold")


wn = trtl.Screen()
wn.bgpic(background_image)
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.addshape(pear_image)# Make the screen aware of the new file

drawer = trtl.Turtle()
apple = trtl.Turtle()
pear = trtl.Turtle()
apple.speed(1)

apple.penup()
pear.penup()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def apple_fall(active_apple):
  apple.setheading(270)
  apple.forward(200)
  wn.update()

def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=font_setup)

#-----function calls-----
draw_apple(apple)

wn.onkeypress(apple_fall, "A")
wn.listen
wn.mainloop()