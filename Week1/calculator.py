def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by Zero.")
    return a/b

def calculate(a, operator, b):
    if operator == "+":
        return add(a,b)
    elif operator == "-":
        return subtract(a,b)
    elif operator == "*":
        return multiply(a,b)
    elif operator == "/":
        return divide(a,b)
    else:
        raise ValueError("Invalid operator!")

def main():
    while True:
        print("\n===== SIMPLE CALCULATOR =====")
        print("1. Perform Calculation")
        print("2. Clear")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                operator = input("Enter operator (+, -, *, /): ").strip()
                b = float(input("Enter second number: "))

                result = calculate(a, operator, b)
                print("Result:", result)

            except ValueError as error:
                print("Invalid input:", error)
            except ZeroDivisionError as error:
                print(error)

        elif choice == "2":
            print("Calculator cleared!")

        elif choice == "3":
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
