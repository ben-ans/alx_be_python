first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
operator = input("Echoose the operation +,-,*,/: ")

num1 = int(first_number)
num2 = int(second_number)
match operator:
    case '+':
        results = num1+num2
        print(results)

    case "-":
        results = num1 - num2
        print(results)

    case "*":
        results = num1 * num2
        print(results)

    case "/":

        try:
            results = num1 / num2
            print(results)

        except ZeroDivisionError:
            print("Cannot divide by zero")