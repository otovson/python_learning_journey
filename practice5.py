secret_number = 22
attempts = 0

while True:
    guess = (input("Guess the number(1-50) or 'q' to Quit: "))

    if guess == "q":
        print ("Game ended.")
        break

    if not guess.isdigit():
        print("Please entetr a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess == secret_number:
        print("Correct! You Win!")
        print ("Number of attempts:", attempts)
        break
    elif guess < secret_number:
        print("Wrong! Number is too low.")
    else:
        print ("Wrong! Number is too high.")