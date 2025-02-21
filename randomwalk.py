from turtle import Turtle, Screen , colormode
import random


t=Turtle()
colormode(255)

colors = ["Orange","LightSeaGreen","indigo","purple","CornflowerBlue","DeepSkyBlue","Lime","IndianRed", "Magenta", "Yellow"]
directions=[0, 90, 180, 270]
t.pensize(10)
screen=Screen()
screen.bgcolor("#000000")
t.speed("fastest")

for _ in range(4000):
    t.color(random.choice(colors))
    t.forward(25)
    t.setheading(random.choice(directions))

screen.exitonclick()