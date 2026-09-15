import random

CHOICES = ["Rock", "Paper", "Scissors"]
def get_player_choice():
    while True:
        print("********** CHOOSE **********")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        raw_input_value = input("Enter your choice: ")
        if not raw_input_value.isdigit():
            print("\nInvalid input.")
            print("Please enter 1, 2, or 3.\n")
            continue
        choice_number = int(raw_input_value)

        if choice_number in (1, 2, 3):
            return CHOICES[choice_number - 1]
        else:
            print("\nInvalid choice.")
            print("Please choose 1, 2, or 3.\n")

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    player_wins = (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    )
    if player_wins:
        return "player"
    else:
        return "computer"

def explain_result(player_choice, computer_choice, result):
    beats = {
        "Rock": "Scissors",
        "Scissors": "Paper",
        "Paper": "Rock",
    }
    if result == "draw":
        print("It's a Draw!")
    elif result == "player":
        print(f"{player_choice} beats {beats[player_choice]}!")
        print("You Win!")
    else:
        print(f"{computer_choice} beats {beats[computer_choice]}!")
        print("Computer Wins!")

def display_score(player_score, computer_score, draws):
    """Print the current score in a neat block."""
    print("\n********** SCORE **********")
    print(f"You:      {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws:    {draws}\n")

def ask_play_again():
    while True:
        answer = input("Do you want to play again? (y/n): ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter 'y' or 'n'.\n")

def display_final_score(player_score, computer_score, draws):
    print("\n******************************")
    print("       FINAL SCORE")
    print("******************************\n")
    print(f"You:      {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws:    {draws}\n")
    if player_score > computer_score:
        print("You are the overall winner!")
    elif computer_score > player_score:
        print("Computer wins the game!")
    else:
        print("The game is a draw!")

    print("\nThanks for playing!")


def play_round():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}\n")
    result = determine_winner(player_choice, computer_choice)
    explain_result(player_choice, computer_choice, result)
    return result

def main():
    player_score = 0
    computer_score = 0
    draws = 0
    print("******************************")
    print("    ROCK PAPER SCISSORS")
    print("******************************\n")
    while True:
        result = play_round()
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            draws += 1
        display_score(player_score, computer_score, draws)
        if not ask_play_again():
            break
        print()
    display_final_score(player_score, computer_score, draws)

main()
