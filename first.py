def multiply(num, num2):
    return num * num2

re = "y"

while re != "n":
    num = input("Please type a number: ")
    while not num.isnumeric():
        print("That's not a number!")
        num = input("Please type a number: ")
    num2 = input("Please type another number: ")
    while not num2.isnumeric():
        print("That's not a number!")
        num2 = input("Please type another number: ")
    result = multiply(int(num), int(num2))
    print(f"{num} x {num2} = {result}")
    re = input("Would you like to do another multiplication? (y/n) ")
    if re == "n":
        print("Thank you for playing!")
        break