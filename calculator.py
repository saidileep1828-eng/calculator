def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def main():
    while True:
        print("\n==========================")
        print("      CALCULATOR APP")
        print("==========================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using Calculator.")
            break

        if choice in ("1", "2", "3", "4"):
            num1 = get_number("Enter First Number: ")
            num2 = get_number("Enter Second Number: ")

            if choice == "1":
                result = add(num1, num2)
                operation = "Addition"
            elif choice == "2":
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == "3":
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == "4":
                result = divide(num1, num2)
                operation = "Division"

            if choice == "4" and result is None:
                print("Cannot divide by zero!")
            else:
                print(f"{operation} result = {result}")
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
