# n x 1 stars
n = int(input("Enter the number of stars: "))
print("Stars in one line")
for i in range(n):
    print("*", end = ' ')
print()

# stars and Xs
print("Stars and Xs in one line")
for i in range(n):
    print("X", end= ' * ')
print()

# 10 x 10 stars
print("10 x 10 stars")
for i in range (10):
    if i % 2 == 0:
        for x in range(5):
            print ("X ", end = '* ')
        print ()
    else:
        for y in range(5):
            print ("* ", end = 'X ')
        print ()
print()
