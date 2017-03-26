"""
The previous examples were all fairly simple, and if you're like me 
they were still hard to wrap my head around. These visualizations should help.
"""
import turtle


def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
draw_spiral(my_turtle, 100)
my_win.exitonclick()