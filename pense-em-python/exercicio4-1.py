import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    t.pu()
    t.lt(90)
    t.fd(300)
    t.rt(90)
    t.pd()
    for i in range(n):
        t.fd(length)
        t.lt(360 - 360/n)

def arc(t, length, angle):
    t.pu()
    t.lt(90)
    t.fd(300)
    t.rt(90)
    t.pd()

    lados_impressos = int(100 / (360 / angle))

    for i in range(lados_impressos):
        t.fd(length)
        t.lt(360 - 360/100)


bob = turtle.Turtle()

arc(bob, 10, 45)

turtle.mainloop()