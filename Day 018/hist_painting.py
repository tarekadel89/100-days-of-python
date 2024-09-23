import colorgram
import random
import turtle as t

# Extract 20 colors from an image.
SOURCE_COLORS = colorgram.extract('day 018\\source_image.jpg', 20)
My_COLORS = []
PADDING_BOTTOM = 25
PADDING_TOP = 20
PADDING_SIDE = 50
PADDING_HORIZONTAL = 50
PADDING_VERTICAL = 50

for color in SOURCE_COLORS:
    My_COLORS.append((color.rgb.r, color.rgb.g, color.rgb.b))
    
# Create a turtle screen and set background color.
t.colormode(255)
my_turtle = t.Turtle()
my_turtle.hideturtle()
my_turtle.speed(0)
my_screen = t.Screen()

my_turtle.teleport(-my_screen.window_width()/2 + PADDING_SIDE, -my_screen.window_height()/2 + PADDING_BOTTOM)

while my_turtle.ycor() < my_screen.window_height()/2 - PADDING_TOP:
    while my_turtle.xcor() < my_screen.window_width()/2 - PADDING_SIDE:
        my_turtle.dot(20,random.choice(My_COLORS))
        my_turtle.teleport(my_turtle.xcor() + PADDING_HORIZONTAL , my_turtle.ycor())
    my_turtle.teleport(-my_screen.window_width()/2 + PADDING_SIDE, my_turtle.ycor() + PADDING_HORIZONTAL)


my_screen.mainloop()