from turtle import *

colors_list = ['red', 'blue', 'brown', 'yellow', 'grey']

speed(-1)
for i in range(3,8):
    color(colors_list[i-3])
    for a in range(i):
        forward(100)
        left(360/i)

mainloop()
