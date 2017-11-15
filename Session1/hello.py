a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = (b ** 2) - (4 * a * c)
if a == 0:
    x = -c / b
    print("x = ", x)
else:
    if d < 0:
        print ("No result")
    elif d == 0:
        x = -b / 2*a
        print("x = ", x)
    else:
        x1 = (-b + d**0.5) / 2*a
        x2 = (-b - d**0.5) / 2*a
        print("2 solutions:, x1={0}, x2={1}".format(x1,x2))
