from turtle import *

colors_list = ['red', 'blue', 'brown', 'yellow', 'grey']

penup()
left(180)
forward(150)
pendown()
left(180)
for i in range (5):
    forward(90)
    color(colors_list[i])
    for a in range(2):
        begin_fill()
        left(90)
        forward(150)
        left(90)
        forward(90)
        end_fill()
mainloop()
