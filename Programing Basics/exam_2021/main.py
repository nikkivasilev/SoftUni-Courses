import turtle


def wining():
    turtle.speed(1000)
    turtle.color('green')
    for i in range(195):
        turtle.circle(360 - i, 25)
        turtle.left(90)
        turtle.circle(360 - i, 25)
        turtle.left(60)


wining()
turtle.mainloop()