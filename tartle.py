from turtle import *

tracer(2)
bgcolor("black")
c=["red" ,"orange"]
pensize(2)

for i in range(600):
    color(c[i%2])
    if i % 5 == 0:
        left(3)
    forward(165)
    left(360/5)
done()

