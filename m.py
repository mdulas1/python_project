import turtle

class MovingTurtle:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("maawiya")
        self.screen.setup(width=800, height=600)
        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.color("red")
        self.t.speed(1)
        self.setup_controls()

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.move_up, "Up")
        self.screen.onkey(self.move_down, "Down")
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")

    def move_up(self):
        self.t.setheading(90)
        self.t.forward(20)

    def move_down(self):
        self.t.setheading(270)
        self.t.forward(20)

    def move_left(self):
        self.t.setheading(180)
        self.t.forward(20)

    def move_right(self):
        self.t.setheading(0)
        self.t.forward(20)

    def run(self):
        self.screen.mainloop()

if __name__ == "__main__":
    moving_turtle = MovingTurtle()
    moving_turtle.run()