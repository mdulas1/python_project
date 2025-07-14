from turtle import*
#from random import*

#pencil = Turtle()
#for i in range(200):
 ##  x = randint(-200,200)
   # y = randint(-200,200)

    #pencil.up()
    #pencil.goto(x,y)
    #pencil.down()
#
 #   pencil.circle(radius)

#done()


t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()


def triangle(t,color):
    t.color()
    t.begin_fill()
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

turtle = [t1,t2,t3,t4]

for t in turtle:
    y = 100
    t.up()
    t.goto(0,y)
    down()
    y-= 100
    
triangle(t1,"red")
triangle(t2,"red")
triangle(t3,"red")
triangle(t4,"red")

done()
