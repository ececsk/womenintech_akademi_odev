import random

player_score = computer_score = computer_choice = 0

def print_result(winner = "Computer"):
    print(f"Computer Choice: {computer_choice}\n\nWinner: {winner}")
    global player_score, computer_score
    if winner == "Computer":
        computer_score += 100
    else:
        player_score += 100
print("\nWelcome to Rock Paper Scissors Game!\n" + "-"*37)

print("Winning rules of the Rock-Paper-Scissor game: \nRock vs Paper -> paper wins \n Rock vs Scissor -> Rock wins \nPaper vs Scissor -> Scissor wins\n\n")

while True:
    print("\n1 - Rock\n2 - Paper \n3 - Scissors\n\nIf you want to exit the game, enter a value other than these values.\n ")
    player_choice = int(input("Enter your choice: "))

    computer_choice = random.choice([1, 2, 3])

    if player_choice == computer_choice:
        print("Player and computer made the same choice, play again ")
    elif player_choice == 1:
        if computer_choice == 2:
            print_result()
        elif computer_choice == 3:
            print_result("Player")
    elif player_choice == 2:
        if computer_choice == 1:
            print_result("Player")
        elif computer_choice == 3:
            print_result()
    elif player_choice == 3:
        if computer_choice == 1:
            print_result()
        elif computer_choice == 2:
            print_result("Player")
    else:
        break

print(f"\n\nPlayer Score: {player_score} - Computer Score: {computer_score}")

if player_score > computer_score: print("Winner: Player")
elif player_score < computer_score: print("Winner: Computer")
else: print("Player and Computer won the same score! ")