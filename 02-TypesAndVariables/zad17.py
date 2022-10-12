h = int(input("Your height in cm: "))

inch = h * 0.393700787
feet = inch /12
inch = inch %12
print(inch)
print(f"I am {h}cm tall, i.e. {int(feet)} feet and {round(inch)} inches.")