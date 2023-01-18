import random

options = {1: "rock", 2: "paper", 3: "scissors",}


def main():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = options[choose_gesture()]
        print(f"You chose {player_choice.title()}")
        computer_choice = options[random.randint(1,3)]
        print(f"The computer opponent chose {computer_choice.title()}!")

        result = validate_winner(player_choice, computer_choice)
    
        if result == player_choice:
            print(f"Player wins - {player_choice} beats {computer_choice}")
            player_score += 1
        elif result == computer_choice:
            print(f"Computer wins - {computer_choice} beats {player_choice}")
            computer_score += 1
        else:
            print(result)
    
        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

        new_game = input("Do you want to play another game (y)/(n)?\n").lower()

        if new_game == "n":
            print("Thank you for the good game!")
            break
    

def choose_gesture():
    while True:
        try:
            choice = int(input("Please choose Rock(1), Paper(2) or Scissors(3)!\n"))
            if choice in options:
                break
        except ValueError:
            print("Wrong input, try another one. You need to enter a number between 1 and 3!")

    return choice

    
def validate_winner(player_choice, computer_choice):
    winner = None
    if player_choice == computer_choice:
        winner = "It's a draw!"
    elif player_choice == "rock" and computer_choice != "paper":
        winner = player_choice
    elif player_choice == "scissors" and computer_choice != "rock":
        winner = player_choice
    elif player_choice == "paper" and computer_choice != "scissors":
        winner = player_choice
    else:
        winner = computer_choice
    return winner  

    
if __name__ == "__main__":
    main()
