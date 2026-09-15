def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_number():
    while True:
        text = input("Enter a number: ")
        try:
            return int(text)
        except ValueError:
            print("Invalid input.")
            print("Please enter a whole number.\n")


def print_menu():
    print("******************************")
    print("    EVEN/ODD & PRIME CHECKER")
    print("******************************")
    print()
    print("1. Check Even or Odd")
    print("2. Check Prime")
    print("3. Check Both")
    print("4. Exit")
    print()

def main():
    running = True
    while running:
        print_menu()
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            number = get_number()
            result = check_even_odd(number)
            print(f"\n{number} is {result}.\n")
        elif choice == "2":
            number = get_number()
            if check_prime(number):
                print(f"\n{number} is a Prime number.\n")
            else:
                print(f"\n{number} is Not a Prime number.\n")
        elif choice == "3":
            number = get_number()
            result = check_even_odd(number)
            print(f"\n{number} is {result}.")
            if check_prime(number):
                print(f"{number} is a Prime number.\n")
            else:
                print(f"{number} is Not a Prime number.\n")
        elif choice == "4":
            print("Thank you for using the program!")
            running = False
        else:
            print("Invalid choice.")
            print("Please select an option from 1 to 4.\n")
            continue
        if running:
            again = input("Do you want to check another number? (y/n): ").strip().lower()
            print()
            if again != "y":
                print("Thank you for using the program!")
                running = False


if __name__ == "__main__":
    main()
