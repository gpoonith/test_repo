#!/usr/bin/python3
#To put in Github

while True:
    print("Options: ")
    print("Enter 'add' to add two numbers")
    print("Enter 'substract' to substract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to leave")
    user_input=input(":")

    if user_input == "quit":
        print("Quit Option Selected!")
        break
    else:
        num1 = int(input("Enter the first Number: "))
        num2 = int(input("Enter the Second Number: "))

        if user_input == "add":
            sum1 = num1 + num2
            print("The sum is ", sum1)

        elif user_input == "substract":
            substract = num1 - num2
            print("The result is: ", substract)

        elif user_input == "multiply":
            multiply = num1 * num2
            print("The result is: ", multiply)

        elif user_input == "divide":
            divide = num1 / num2
            print("The result is: ", divide)

        else:
            print("Wrong Values input")
