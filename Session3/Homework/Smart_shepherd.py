flock = [40, 15, 125, 169, 44, 18, 79, 82, 24, 155, 95]
print("Hello, I'm Vietanh the shepherd, and here are the sheep sizes in my flock:\n",flock, sep = '')

print()

biggest_sheep = 0
for i in range (len(flock)):
    if flock[i] > biggest_sheep:
        biggest_sheep = flock[i]
print("Now my biggest sheep has the size of", biggest_sheep,", let's sheer it.")

flock[flock.index(biggest_sheep)] = 8
print("After sheering, here is my flock:\n", flock, sep = '')

print()

n = int(input("How many more months do you want to calculate? "))
for a in range(n):
    print("MONTH ", a + 1, " :", sep='')
    for b in range (len(flock)):
        flock[b] += 50
    print("One month has passed, my flock has grown a lot:\n",flock, sep = '')
    biggest_sheep = 0

    for c in range (len(flock)):
        if flock[c] > biggest_sheep:
            biggest_sheep = flock[c]
    print("Now my biggest sheep has the size of", biggest_sheep,", let's sheer it.")

    flock[flock.index(biggest_sheep)] = 8
    print("After sheering, here is my flock:\n", flock, sep = '')
    print('*' * 40)

    print("OK, let sell this stupid flock to travel the world.")
    total_size = 0
    for x in range(len(flock)):
        total_size += flock[x]
    print("Total size of my flock: ", flock)
    print("I would get", total_size, '* 2$ =', total_size * 2)
