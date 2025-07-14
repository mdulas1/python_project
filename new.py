from turtle import*

pencil = Turtle()
def square(p, size,color):
    p.color(color)
    p.begin_fill()
    for i in range(8): 
     p.forward(size)
     p.right(40)
     p.end_fill()

    done()

square(pencil, 100, "purple")    