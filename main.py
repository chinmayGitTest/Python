def classify_number(number):
    if number < 0:
        print("The number is negative.")
    elif number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")

user_input = int(input("Enter an integer: "))

classify_number(user_input)
