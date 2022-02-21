# Rock Paper Scissors game

from random import randint

play_again = True

while play_again == True:

    player_choice_input = input("Choose Rock Paper or Scissors! (R/P/S): ")

    player_choice = "Unspecified."

    if player_choice_input == 'R' or 'r':
        player_choice = "rock"
    elif player_choice_input == 'S' or 's':
        player_choice = "scissors"
    elif player_choice_input == 'P' or 'p':
        player_choice = "paper"
    else:
        print("Invalid input.")
    print("You've chosen " + player_choice)

    options = ["rock","paper","scissors"]

    computer_choice_int = randint(0,2)

    computer_choice = options[computer_choice_int]

    print("The PC picked " + computer_choice)

    if player_choice == computer_choice:
        print(f"Both players selected {player_choice}. It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    user_play_again = input("Play again?  Y/N) ")

    if user_play_again == "Y" :
        print("Let's go again!")
    elif user_play_again == "N" :
        play_again == False
        print("Let's take a break.")
    else :
        print("Invalid Input.")
