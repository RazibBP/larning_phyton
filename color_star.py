import turtle as s
import colorsys as cs

s.setup(700, 700)
s.speed(0)
s.tracer(10)
s.width(1.4)
s.bgcolor("black")

for i in range(25):
    for j in range(15):
        s.color(cs.hsv_to_rgb(j/15 , i/25 ,1))
        s.right(90)
        s.circle(160 - i*3 ,90)
        s.left(90)
        s.circle(160 - i*3 , 90)
        s.right(180)
        s.circle(35,24)

s.hideturtle()
s.done()