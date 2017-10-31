print("Hello, I am the Factorial Calculator")
n = int(input("Enter a number "))

x = 1
for i in range (1, n + 1):
    x *= i
print("The result is", x)
