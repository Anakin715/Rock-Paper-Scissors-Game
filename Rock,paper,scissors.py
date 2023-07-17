import random
import time
while True:
    i=0
    print("rock")
    time.sleep(1)
    print("paper")
    time.sleep(1)
    print("scissors")
    time.sleep(1)
    print("SHOOT!")
    choices = ['rock','paper','scissors']
    computer = random.choice(choices)
    player = input("Enter your choice: ").lower()
    while player not in choices:
         player = input("Invalid choice, Try again? ").lower()
    time.sleep(1)
    print(player," : ",computer)
    if computer == "paper" and player == "rock":
        time.sleep(0.5)
        print("You LOST!")
    elif computer == player:
        time.sleep(0.5)
        print("TIE!")
    elif computer == "paper" and player == "scissors":
        time.sleep(0.5)
        print("You WON!")
    elif computer == "rock" and player == "paper":
        time.sleep(0.5)
        print("You WON!" )
    elif computer == "rock" and player == "scissors":
        time.sleep(0.5)
        print("You LOST!")
    elif computer == "scissors" and player == "rock":
        time.sleep(0.5)
        print("You WON!")
    elif computer == "scissors" and player == "paper":
        time.sleep(0.5)
        print("You LOST!")
    play_again = input("Play again (yes/no)").lower()

    if play_again != "yes":
        break
print("Bye!")

