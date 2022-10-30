import random

def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors):")
    options = ["rock", "paper", "scissors"]
    if player_choice in options:
        computer_choice = random.choice(options)
        choices = {"player": player_choice, "computer": computer_choice}
        return choices
    else:
        print("Invalid Input")
        exit()


def check_win(player, computer):
    print(f"You chose {player} computer chose {computer}")
    if player == computer:
        return "Its a draw!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes Scissors! You Win"
        else:
            return "Paper covers Rock! You Lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers Rock! You Win!"
        else:
            return "Scissors cuts paper! You Lose"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You Win!"
        else:
            return "Rock smashes Scissors! You Lose"


choices = get_choices()
results = check_win(choices["player"], choices["computer"])
print(results)
