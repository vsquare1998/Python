import random


def vs_computer():
    print("*****You Are Playing Agains Computer!!*****")
    player_score = 0
    computer_score = 0
    game = ["stone", "paper", "scissor"]
    while True:
        print("Select: 1 For Stone\n \t2. For Paper\n \t 3. For Scissor\n \t4.exit")
        player_choice = int(input("Enter Your Choice:"))
        if player_choice == 1:
            print("You Selected Stone")
        elif player_choice == 2:
            print("You Selected Paper")
        elif player_choice == 3:
            print("You Selected Scissor")
        computer_choice = random.choice(game)
        if player_choice != 4:
            print(f"Computer Selected {computer_choice}")
        if (
            (player_choice == 1 and computer_choice == "stone")
            or (player_choice == 2 and computer_choice == "paper")
            or (player_choice == 3 and computer_choice == "scissor")
        ):
            print("Resulr: Draw")
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
        elif player_choice == 4:
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
            print("Invalid Input!")
            continue


vs_computer()
