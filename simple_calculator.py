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

def show_menu():
    print("******************************")
    print("      SIMPLE CALCULATOR")
    print("******************************")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print()

def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input.")
            print("Please enter a valid number.")
            print()

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        print()
        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice.")
            print("Please select an option from 1 to 5.")
            print()
            continue
        if choice == "5":
            print("Thank you for using the calculator!")
            break
        first_number = get_number("Enter first number: ")
        second_number = get_number("Enter second number: ")
        print()
        if choice == "1":
            result = add(first_number, second_number)
            symbol = "+"
        elif choice == "2":
            result = subtract(first_number, second_number)
            symbol = "-"
        elif choice == "3":
            result = multiply(first_number, second_number)
            symbol = "*"
        elif choice == "4":
            result = divide(first_number, second_number)
            symbol = "/"
            if result is None:
                print("Cannot divide by zero.")
                print("Please enter a non-zero second number.")
                print()
                again = input("Do you want to perform another calculation? (y/n): ")
                print()
                if again.lower() != "y":
                    print("Thank you for using the calculator!")
                    break
                continue
        print(f"Result: {first_number} {symbol} {second_number} = {result}")
        print()
        again = input("Do you want to perform another calculation? (y/n): ")
        print()
        if again.lower() != "y":
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main()
