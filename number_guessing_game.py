import random


def play_game(lower, upper):
    secret_number = random.randint(lower, upper)
    attempts = 0
    guess = None
    print(f"\nI have selected a number between {lower} and {upper}.\n")
    while guess != secret_number:
        user_input = input("Enter your guess: ")
        if not user_input.isdigit():
            print("Please enter a valid number.\n")
            continue
        guess = int(user_input)
        if guess < lower or guess > upper:
            print(f"Please enter a number between {lower} and {upper}.\n")
            continue
        attempts = attempts + 1
        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print("\nCongratulations! You guessed the number!")
            print(f"Number of attempts: {attempts}\n")
    return attempts


def choose_difficulty():
    print("********** DIFFICULTY **********")
    print("1. Easy   -> Number between 1 and 50")
    print("2. Medium -> Number between 1 and 100")
    print("3. Hard   -> Number between 1 and 500")
    choice = input("Choose difficulty (1/2/3): ")
    if choice == "1":
        return 1, 50
    elif choice == "3":
        return 1, 500
    else:
        return 1, 100


def main():
    print("******************************")
    print("    NUMBER GUESSING GAME")
    print("******************************")
    playing = True
    while playing:
        lower, upper = choose_difficulty()
        play_game(lower, upper)
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != "y":
            playing = False
    print("\nThanks for playing!")

main()
