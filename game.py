import random

def play_round(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player"
    else:
        return "Computer"

def play_game(num_rounds):
    player_score = 0
    computer_score = 0

    for _ in range(num_rounds):
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        winner = play_round(player_choice)

        if winner == "Player":
            player_score += 1
            print("You win this round!")
        elif winner == "Computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

        if player_score == num_rounds // 2 + 1:
            print("You win the game!")
            break
        elif computer_score == num_rounds // 2 + 1:
            print("Computer wins the game!")
            break

    if player_score == computer_score:
        print("The game is a tie!")

if __name__ == "__main__":
    num_rounds = int(input("Enter the number of rounds (3 or 5): "))
    play_game(num_rounds)