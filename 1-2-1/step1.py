# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"

#-----initialize turtle-----
spot = t.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)

#-----game functions--------


#-----events----------------

wn = t.Screen()
wn.mainloop()