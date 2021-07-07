import turtle
wn = turtle.Screen()
wn.bgcolor("white")
alex = turtle.Turtle()
distance = 50
for _ in range(50):
    alex.forward(distance)
    alex.right(90)
    distance += 10

wn.exitonclick()