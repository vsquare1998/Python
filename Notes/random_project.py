import random


def stone_paper_scissor():
    game = ["stone", "paper", "scissor"]
    player_score = 0
    computer_score = 0
    # player_choice = int(
    #     input("Enter 1 for stone\n 2 for paper\n 3 for scissor\n -1 for exit:\n")
    # )
    # print(f"You have selected: {player_choice}")
    # computer_choice = random.choice(game)
    # print(f"Computer has selected: {computer_choice}")

    while True:
        player_choice = int(
            input("Enter 1 for stone\n 2 for paper\n 3 for scissor\n -1 for exit:\n")
        )
        print(f"You have selected: {player_choice}")
        computer_choice = random.choice(game)
        print(f"Computer has selected: {computer_choice}")

        if player_choice in [1, 2, 3, -1]:

            if (
                (player_choice == 1 and computer_choice == "stone")
                or (player_choice == 2 and computer_choice == "paper")
                or (player_choice == 3 and computer_choice == "scissor")
            ):
                print("Result: Draw")
                continue
            elif (
                (player_choice == 1 and computer_choice == "paper")
                or (player_choice == 2 and computer_choice == "scissor")
                or (player_choice == 1 and computer_choice == "stone")
            ):
                print("Computer won")
                computer_score += 1
                continue
            elif (
                (player_choice == 1 and computer_choice == "scissor")
                or (player_choice == 2 and computer_choice == "stone")
                or (player_choice == 3 and computer_choice == "paper")
            ):
                print("You won")
                player_score += 1
                continue
            elif player_choice == -1:
                print(f"Your Score:{player_score}")
                print(f"Computer Score:{computer_score}")
                if player_score > computer_score:
                    print("You won!")
                    break
                elif player_score == computer_score:
                    print("Draw!")
                    break
                else:
                    print("Computer Won!")
                    break
        else:
            print("Invalid choice")
            break


stone_paper_scissor()
