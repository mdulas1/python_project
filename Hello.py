from turtle import*

t1 = Turtle()
t1.color()
t1.width(4)


t1.begin_fill()
for i in range(4):
    t1.forward(150)
    t1.left(300)
    t1.backward(60)
    t1.right(133)
    t1.backward(200)
    t1.forward(100)
    t1.forward(100)

    t1.end_fill()

    done()