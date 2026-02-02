# from turtle import Turtle, Screen
#
#
# my_turtle = Turtle()
# other_turtle = Turtle()
#
# other_turtle.color("blue")
# other_turtle.shape("circle")
# other_turtle.forward(200)
#
# screen = Screen()
#
# my_turtle.shape("turtle")
# my_turtle.color("red")
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(45)
# my_turtle.forward(300)
#
# screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()

table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])

table.align["City name"] = 'l'
table.align["Annual Rainfall"] = 'r'


print(table)