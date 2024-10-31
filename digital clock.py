import turtle
import time

# Set up the window
win = turtle.Screen()
win.title("Digital Clock")
win.bgcolor("gray")
win.setup(width=600, height=300)
win.tracer(0)

# Create the turtle for drawing the clock
clock_turtle = turtle.Turtle()
clock_turtle.hideturtle()
clock_turtle.color("black")

# Function to draw clock
def draw_clock():
    while True:
        current_time = time.strftime("%H:%M:%S")
        clock_turtle.clear()
        clock_turtle.write(current_time, align="center", font=("Courier", 50, "bold"))
        clock_turtle.write("Group 1 Digital clock.")
        win.update()
        time.sleep(1)

# Start drawing the clock
draw_clock()