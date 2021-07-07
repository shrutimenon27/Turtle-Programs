import turtle
wn = turtle.Screen()
wn.bgcolor("white")
minion = turtle.Turtle()
distance = 50
for _ in range(50):
    minion.forward(distance)
    minion.right(90)
    distance += 10

wn.exitonclick()