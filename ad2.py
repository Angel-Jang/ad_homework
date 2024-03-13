import turtle

def movePen(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

movePen(-175, 0)
turtle.color("#0081C8") # "blue"


turtle.fillcolor("#0081C8")
turtle.begin_fill()
turtle.circle(80)
movePen(-175, 15)
turtle.circle(65)
turtle.end_fill()


movePen(-87, -80)
turtle.color("#FCB131") # "yellow"


turtle.fillcolor("#FCB131")
turtle.begin_fill()
turtle.circle(80)
movePen(-87, -65)
turtle.circle(65)
turtle.end_fill()


movePen(0, 0)
turtle.color("#000000") # "black"

turtle.fillcolor("#000000")
turtle.begin_fill()
turtle.circle(80)
movePen(0, 15)
turtle.circle(65)
turtle.end_fill()


movePen(87, -80)
turtle.color("#00A651") # "green"


turtle.fillcolor("#00A651")
turtle.begin_fill()
turtle.circle(80)
movePen(87, -65)
turtle.circle(65)
turtle.end_fill()


movePen(175, 0)
turtle.color("#EE334E") # "red"


turtle.fillcolor("#EE334E")
turtle.begin_fill()
turtle.circle(80)
movePen(175, 15)
turtle.circle(65)
turtle.end_fill()

turtle.done()
