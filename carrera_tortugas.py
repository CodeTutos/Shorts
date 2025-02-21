from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
screen.bgcolor("#000000")

is_race_on = False

colors = ["red","orange","yellow","green","gray","purple"]
options = ["r","n","a","v","g","p"]

racers = []

for i in range(6):
    t = Turtle(shape= "turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x= -230, y =50-i*20)
    racers.append(t)

while not is_race_on:
    user_bet = screen.textinput(title = "Hola", prompt = 'Qué tortuga ganará la carrera? Ingresa un color: \n r:rojo,n: naranja,a:amarillo, v:verde, g:gris, p:púrpura')
    if user_bet in options:
        is_race_on = True
ganador = ""

while is_race_on:
    for i in racers:
        random_distance = random.randint(0,10)
        i.fd(random_distance)
        if list(i.pos())[0] >= 230:
            print(f"Gano el color: {list(i.color())[0]}!")
            ganador = list(i.color())[0]
            is_race_on = False
text = Turtle()
text.hideturtle()
text.color("white")
index = options.index(user_bet)

if ganador== colors[index]:
    text.write("GANASTE!.", move=False, align='center', font=('Arial', 30, 'normal'))
else:
    text.write("PERDISTE!.", move=False, align='center', font=('Arial', 30, 'normal'))
screen.exitonclick()