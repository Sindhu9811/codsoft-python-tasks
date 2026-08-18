def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def main():
    print("===================================")
    print("       SIMPLE CALCULATOR")
    print("===================================")

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select 1-5.")
            continue

        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            result = add(number1, number2)
            symbol = "+"

        elif choice == "2":
            result = subtract(number1, number2)
            symbol = "-"

        elif choice == "3":
            result = multiply(number1, number2)
            symbol = "*"

        else:
            result = divide(number1, number2)
            symbol = "/"

        print("\n-----------------------------------")

        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: {number1} {symbol} {number2} = {result}")

        print("-----------------------------------")


if __name__ == "__main__":
    main()
