a = int(input("Number of circles that u want? "))
turning_angle = float(360/a)
from turtle import *

speed(-1)

for i in range(a):
    circle(50)
    right(turning_angle)

mainloop()
