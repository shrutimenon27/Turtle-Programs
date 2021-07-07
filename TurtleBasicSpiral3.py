import turtle
wn = turtle.Screen()
wn.bgcolor("white")
minion = turtle.Turtle()
minion.shape("turtle")
minion.up()
minion.color("red")
distance = 20
for _ in range(90):
    minion.forward(distance)
    minion.right(25)
    minion.stamp()
    distance += 2
wn.exitonclick()