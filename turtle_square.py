import turtle as s

s.speed(0)
s.bgcolor("black")
s.pencolor("green")


def square(x ,y):
    for j in range(4):
        s.forward(x)
        s.right(y)
for i in range(80):
    square(170 , 90)
    s.right(5)
    s.circle(50)
    s.right(50)
    s.hideturtle()
s.done()