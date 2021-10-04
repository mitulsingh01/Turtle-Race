from turtle import Turtle, Screen, width
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Who are you betting on?", prompt="Who do you think is gonna win? Choose the color: ")
bet = bet.lower()
colors = ["Red", "Blue", "Green", "Orange" , "Yellow", "Purple"]
y_pos = [-125,-75,-25,25,75,125]
turtles = []

if bet:
    is_race_on = True

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index]) 
    turtles.append(new_turtle)  

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == bet:
                print(f"{winner} won! You were Right.")
            else:
                print(f"{winner} won! Sorry, you Lost.")

            is_race_on = False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)






screen.exitonclick()
