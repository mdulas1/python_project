from http.client import MOVED_PERMANENTLY
import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Catch the Falling Objects")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Create the falling objects
objects = []
for _ in range(10):
    obj = turtle.Turtle()
    obj.shape("circle")
    obj.color("red")
    obj.penup()
    obj.speed(0)
    obj.setposition(random.randint(-390, 390), random.randint(100, 400))
    objects.append(obj)

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= 20 
    if x < -390:
        x = -390
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 390:
        x = 390
    player.setx(x)

def move_up():
    x = player.xcor()
    x -=20
    if x < -390:
        x = -390
    player.setx(x)


def move_up():
    x = player.xcor()
    x -=20
    if x < 390:
        x = 390
    player.setx(x)

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")


# Main game loop
while True:
    for obj in objects:
        y = obj.ycor()
        y -= 3
        obj.sety(y)

        # Check if the object is caught by the player
        if obj.distance(player) < 20:
            obj.setposition(random.randint(-390, 390), random.randint(100, 400))

        # Check if the object has fallen off the screen
        if y < -300:
            obj.setposition(random.randint(-390, 390), random.randint(100, 400))

    screen.update()