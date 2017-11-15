h_cm = int(input("Your height(cm) is: "))
w = int(input("Your weight(kg) is: "))
h_m = h_cm / 100
BMI = w / (h_m ** 2)

if BMI < 16:
    print("You are severely underweight. Pls eat more")
elif BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("Your body is normal")
elif BMI < 30:
    print("You are overweight")
else:
    print("You are obese. Pls take more excercises")
