import turtle
import random
t1=turtle.Turtle()
turtle.setworldcoordinates(0,0,40,40)
#density=float(input("enter a number(0.1-1): "))
#percentPine=float(input("enter a number(0-1): "))
t1.speed(50)
probCatch=0.45
firerand=random.random()
turtle.tracer(8,0)
turtle.update()


def fireconditon():
    n=0
    while n <= 100:
        a=random.random()
        if a < probCatch:
            return True
            update()
        else:
            return False
        n+=1
fireconditon()
m=20
n=20
def update():
    if True:
        t1.goto(m,n)
        t1.color("red")
        t1.stamp()
