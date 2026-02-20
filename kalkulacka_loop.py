while True:
    num1 = input("Set first number (or 'q' for end): ")
    
    if num1 == "q":
        print("Program is shutting down.")
        break
    
    num2 = input("Set second number: ")
    operation = input("set operation (+, -, *, /): ")

    num1 = int(num1)
    num2 = int(num2)

    if operation == "+":
        print("Result:", num1 + num2)

    elif operation == "-":
        print("Result:", num1 - num2)

    elif operation == "*":
        print("Result:", num1 * num2)

    elif operation == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Devision by zero is not allowed!")

    else:
        print("Operation is not allowed!")