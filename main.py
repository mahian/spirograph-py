from turtle import *
bgcolor('black')
pensize(2)
speed(100)

for i in range(12):
    for colors in ['red', 'green', 'blue']:
        color(colors)
        circle(100)
        left(10)
done()