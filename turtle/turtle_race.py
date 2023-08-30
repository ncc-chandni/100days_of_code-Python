from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")
colors = ["red", "orange","yellow","green","blue","purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.penup()
    new_turtle.goto(x= -230, y = y_pos[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for Turtle in all_turtles:
        if Turtle.xcor() > 230:
            is_race_on = False  
            winner = Turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The winner is  {winner} turtle")
            else:
                print(f"You lost. The winner is {winner} turtle")
        
        move = random.randint(0,20)
        Turtle .forward(move)

screen.exitonclick()