import turtle

t = turtle.Pen()
turtle.hideturtle()
turtle.speed(0)

turtle.bgcolor("red")

turtle.title("cursedddcube")

t.width(3)
for i in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.sety(50)
t.setx(50)
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)

t.goto(0, 0)
t.goto(50, 50)

t.goto(50, 150)
t.goto(0, 100)

t.goto(100, 100)
t.goto(150, 150)

t.goto(150, 50)
t.goto(100, 0)

for x in range(30, 100, 5):
    turtle.color('black')
    style = ('Courier', x, 'italic')
    turtle.write('CURSED!', font=style, align='center')
turtle.hideturtle()

turtle.Screen().exitonclick()
