import turtle
wn = turtle.Screen()
wn.bgcolor("black")
minion = turtle.Turtle()
minion .color("white")
distance = 50
angle = 90
for _ in range(100):
    minion.forward(distance)
    minion.right(angle)
    distance += 10
    angle -= 1
wn.exitonclick()