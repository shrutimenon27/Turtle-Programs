import turtle
wn = turtle.Screen()
wn.bgcolor("black")
alex = turtle.Turtle()
alex.color("white")
distance = 50
angle = 90
for _ in range(100):
    alex.forward(distance)
    alex.right(angle)
    distance += 10
    angle -= 1
wn.exitonclick()