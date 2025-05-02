#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: March , 2025

# adds random module
import random

# array holding options and different outcomes of the game
interactions = ["lose!", "tied!", "win!"]
rock = [1, 0, 2]
paper = [2, 1, 0]
scissors = [0, 2, 1]

def main():

    # variables used to display the amount of wins/losses you have at the end
    wins = 0
    losses = 0

    # loops game until user stops it
    while True:

        # asks user to choose a move
        user_choice = input("Choose rock(0), paper(1), or scissors(2): ")

        # try catch responsible for the move input section
        try:

            # converts users input into integer
            user_choice = int(user_choice)

            # randomizes the computers move
            comp_choice = random.randint(0, 2)

            # large nested if block determining the outcome of the game using the previous arrays
            if user_choice <= 2 and user_choice >= 0:
                if comp_choice == 0:
                    print("Opponent chose rock")
                if comp_choice == 1:
                    print("Opponent chose paper")
                if comp_choice == 2:
                    print("Opponent chose scissors")
                if user_choice == 0:
                    print("You chose rock")
                    print("You", interactions[rock[comp_choice]])
                    if rock[comp_choice] == 2:
                        wins += 1
                    if rock[comp_choice] == 0:
                        losses += 1
                if user_choice == 1:
                    print("You chose paper")
                    print("You", interactions[paper[comp_choice]])
                    if paper[comp_choice] == 2:
                        wins += 1
                    if paper[comp_choice] == 0:
                        losses += 1
                if user_choice == 2:
                    print("You chose scissors")
                    print("You", interactions[scissors[comp_choice]])
                    if scissors[comp_choice] == 2:
                        wins += 1
                    if scissors[comp_choice] == 0:
                        losses += 1

            # prints message if input was out of range
            else:
                print(user_choice, "was not in the range 0-2!")

            # asks user if they want to keep playing
            user_quit = input("Play another round? yes(1), no(0): ")

            # nested try catch for valid input
            try:
                user_quit = int(user_quit)
                if user_quit <= 1 and user_quit >= 0:
                    if user_quit == 0:
                        print("Thanks for playing!")
                        print("You won", wins, "times, and lost", losses, "times!")
                        break
                else:
                    print(user_quit, "was not in the range 0-1!")

            # if invalid integer prints this message instead of crashing
            except:
                print(user_quit, "was not a valid integer!")

        # if invalid integer prints this message instead of crashing
        except:
            print(user_choice, "was not a valid integer!")


if __name__ == "__main__":
    main()
