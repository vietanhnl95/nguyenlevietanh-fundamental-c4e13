from turtle import *

speed(-1)
for i in range(3,7):
    angle = (1 - 2/i ) * 180
    for a in range(i):
        if i % 2 == 0:
            color("red")
        else:
            color("blue")
        forward(100)
        left(180-angle)

mainloop()
