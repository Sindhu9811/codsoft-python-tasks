import random


def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the two choices."""

    if user_choice == computer_choice:
        return "tie"

    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"

    return "computer"


def display_result(user_choice, computer_choice, result):
    """Display the choices and result."""

    print("\n" + "=" * 45)
    print("Your choice     :", user_choice.capitalize())
    print("Computer choice :", computer_choice.capitalize())
    print("=" * 45)

    if result == "user":
        print("🎉 You win!")
    elif result == "computer":
        print("😔 You lose!")
    else:
        print("🤝 It's a tie!")


def main():
    """Run the Rock-Paper-Scissors game."""

    user_score = 0
    computer_score = 0
    tie_score = 0

    print("=" * 50)
    print("        ROCK - PAPER - SCISSORS GAME")
    print("=" * 50)

    print("\nGame Rules:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("Same choices result in a tie.")

    while True:
        print("\nChoose one of the following:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_choice = input("\nEnter your choice: ").strip().lower()

        # Allow both words and numbers
        if user_choice == "1":
            user_choice = "rock"
        elif user_choice == "2":
            user_choice = "paper"
        elif user_choice == "3":
            user_choice = "scissors"

        # Validate user input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("\n❌ Invalid choice!")
            print("Please enter rock, paper, scissors, or 1, 2, 3.")
            continue

        # Computer makes a random choice
        computer_choice = get_computer_choice()

        # Determine winner
        result = determine_winner(user_choice, computer_choice)

        # Update score
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            tie_score += 1

        # Display result
        display_result(user_choice, computer_choice, result)

        # Display current score
        print("\nCurrent Score:")
        print("You      :", user_score)
        print("Computer :", computer_score)
        print("Ties     :", tie_score)

        # Ask whether the user wants another round
        while True:
            play_again = input(
                "\nDo you want to play again? (y/n): "
            ).strip().lower()

            if play_again in ["y", "yes"]:
                break

            elif play_again in ["n", "no"]:
                print("\n" + "=" * 45)
                print("             FINAL SCORE")
                print("=" * 45)
                print("You      :", user_score)
                print("Computer :", computer_score)
                print("Ties     :", tie_score)
                print("=" * 45)
                print("Thank you for playing!")
                print("Goodbye! 👋")
                return

            else:
                print("Please enter y for yes or n for no.")


if __name__ == "__main__":
    main()
