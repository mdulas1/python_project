import turtle

class Paddle:
    def __init__(self, position):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=6, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(position)

    def go_up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def go_down(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)

if __name__ == "__main__":
    # Set up the screen
    wn = turtle.Screen()
    wn.title("Pong game")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Create paddles
    left_paddle = Paddle((-350, 0))
    right_paddle = Paddle((350, 0))

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(left_paddle.go_up, "w")
    wn.onkeypress(left_paddle.go_down, "s")
    wn.onkeypress(right_paddle.go_up, "Up")
    wn.onkeypress(right_paddle.go_down, "Down")

    # Main game loop
    while True:
        wn.update()