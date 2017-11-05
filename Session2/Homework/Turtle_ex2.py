from turtle import *

n = int(input("Enter a number: "))
m = n + 3
speed(-1)
for i in range(3,m):
    angle = (1 - 2/i) * 180
    for a in range(i):
        if i % 2 == 0:
            color("red")
        else:
            color("blue")
        forward(100)
        left(180-angle)

mainloop()
