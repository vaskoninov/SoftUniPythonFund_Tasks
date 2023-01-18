import random


def main():

    game()

    print("Thank you!")


def guessing_computer_number(attempts, difficulty):
    number_to_guess = get_number(difficulty)
    print(f"I think of a number in range {difficulty[0]} -{difficulty[1]}")
    counter = 0
    while attempts >= 0:
        if attempts == 0:
            print("Sorry, no more tries!")
            print(f"The number you looked for was {number_to_guess}")
            break
        user_number = user_guess(difficulty)
        if user_number == number_to_guess:
            print(f"You guessed the number - {number_to_guess}")
            print(
                f"Good game! You succeeded in {counter} tries and you are left with {attempts}"
            )
            break
        else:
            if user_number > number_to_guess:
                print("Lower")
            else:
                print("Higher")
        attempts -= 1
        counter += 1

    print("Thank you for the game!")


def game():
    attempts = int(input("How many attempts for guessing right: \n"))
    difficulty = get_difficulty()
    while True:
        guessing_computer_number(attempts, difficulty)
        if not play_again():
            break


def get_number(difficulty):
    number = random.randint(difficulty[0], difficulty[1])
    return number


def user_guess(difficulty):
    while True:
        try:
            user_input = int(
                input(
                    f"Guess a number between {difficulty[0]} - {difficulty[1]}:\n"
                ))
            break
        except ValueError:
            print(
                f"You need to guess a valid integer between {difficulty[0]} - {difficulty[1]}"
            )
            continue
    return user_input


def play_again():
    new_game = input("Do you want to play again? (y)/(n)\n").lower()
    if new_game == "y":
        return True
    else:
        return False


def get_difficulty():
    difficulty = {"a": [1, 100], "b": [1, 1000]}

    choice = input(
        "Please choose difficulty: (a) beginner, (b) professional\n").lower()
    if choice == "a":
        return difficulty["a"]
    else:
        return difficulty["b"]


if __name__ == "__main__":
    main()
