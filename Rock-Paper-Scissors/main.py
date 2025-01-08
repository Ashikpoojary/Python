import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        quit()
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock=0, paper=1, scissor=2
    computer_guess = options[random_number]
    print("Computer picked", computer_guess + ".")

    if user_input == "rock" and computer_guess == "scissors":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_guess == "rock":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_guess == "paper":
        print("You won!")
        user_wins += 1
        continue

    else:
        print("You lost!")
        computer_wins += 1
    
print("You won", user_wins, "times.")
print("You computer won", computer_wins, "times.")
print("Goodbye!")