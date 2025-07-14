from turtle import*

pencil =Turtle()

def triangle(t,color,):
    t.color=(color)
    t.begin_fill()
    for i in range(8):
        t.forward(100)
        t.right(40)
    t.end_fill()
    done()

triangle(pencil,"red")         
