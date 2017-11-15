from random import randint
n = randint (1,100)
loopcon = True
while loopcon:
    x = int(input("Guess my number from 1 to 100 ..."))
    if x == n:
        print("bingo")
        loopcon = False #or use break
    elif x - n > 0 and abs(x-n) > 10:
        print("too large")
    elif x - n > 0 and abs(x-n) < 10:
        print("a bit large")
    elif x - n < 0 and abs(x-n) < 10:
        print("a bit small")
    elif x - n < 0 and abs(x-n) > 10:
        print("too small")
