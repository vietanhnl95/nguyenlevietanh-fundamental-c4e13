#use division:
for i in range(0,16):
    if i % 2 == 0:
        print(i, end=' ')
print ()

#use step:
for i in range(0,16,2):
    print (i, end =' ')
print ()

n = int(input("Enter the number: "))
if n % 2 == 0 and n % 3 != 0:
    print ("Fizz")
if n % 2 != 0 and n % 3 == 0:
    print ("Buzz")
if n % 2 == 0 and n % 3 == 0:
    print ("FizzBuzz")
