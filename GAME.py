import random


def choose_difficulty():
    while True:
        choice = input("Choose difficulty (easy/hard): ").lower()

        if choice == "easy":
            return 10
        elif choice == "hard":
            return 5
        else:
            print("Please enter 'easy' or 'hard'.")


def get_user_guess():
    while True:
        guess = input("Enter a number (1-100) or 'q' to quit: ")

        if guess == "q":
            return None

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100.")
            continue

        return guess


def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = choose_difficulty()
    attempts = 0

    while attempts < max_attempts:
        guess = get_user_guess()

        if guess is None:
            print("Game ended.")
            return None, None

        attempts += 1

        if guess == secret_number:
            print("Correct! You win!")
            print("Attempts used:", attempts)
            return True, attempts

        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

        print("Attempts left:", max_attempts - attempts)

    print("Game over! The correct number was:", secret_number)
    return False, attempts


def main():
    wins = 0
    losses = 0
    high_score = None

    while True:
        result, attempts = play_game()

        if result is True:
            wins += 1

            if high_score is None or attempts < high_score:
                high_score = attempts
                print("🏆 New High Score:", high_score, "attempts!")

        elif result is False:
            losses += 1

        print("Wins:", wins, "| Losses:", losses)

        if high_score is not None:
            print("Current High Score:", high_score, "attempts")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Final score - Wins:", wins, "| Losses:", losses)
            if high_score is not None:
                print("Best game:", high_score, "attempts")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()