try:

    a = int(input("Enter the first number: "))

    b = int(input("enter the second number: "))

    print(f"what kind of opertaion do you want with {a} and {b}")

    op = input("enter operation")
    match op:
        case "+":
            print(f"The result is:{a + b} ")
        case "-":
            print(f"The result is:{a - b} ")
        case "*":
            print(f"The result is:{a * b} ")
        case "/":
            print(f"The result is:{a / b} ")
        case default:
            print("User error")

except Exception as e:
    print("Enter a valid value of a and b ")

