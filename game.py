
import random

import os
from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv

#
# 2) After that, we generally run any setup code, like setting environment variables:
#

load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the "python-dotenv" package docs for more info

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One") # uses the os module to read the specified environment variable and store it in a corresponding python variable


print("Rock, Paper, Scissors, Shoot!")

#user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

user_choice = input(f"Welcome {PLAYER_NAME} to my Rock-Paper-Scissors game...Please choose either 'rock', 'paper', or 'scissors': ")

#print(user_choice)
print("USER CHOICE", user_choice)


# validate the input such that only if it is one of the expected values
#... will continue with the rest of the program
#... otherwise we'll stop the program before it tries to do anyhting else
#... and we'll ask the user to run the program again 

#if (user_choice == "rock"):
if (user_choice == "rock") or (user_choice == "paper") or (user_choice =="scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()


valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE", computer_choice)

#Determining the Winner

# Rock beats Scissors - Note this is the original method I tried on my own. Below, find the more efficient code worked on in class (starting at line 84).

# if (user_choice == "rock") and (computer_choice == "scissors"):
    # print("You win!")

# if (computer_choice == "rock") and (user_choice == "scissors"):
    # print("Oh, the computer won. It's ok!")

#Paper beats Rock

# if (user_choice == "paper") and (computer_choice == "rock"):
    # print("You win!")

# if (computer_choice == "paper") and (user_choice == "rock"):
    # print("Oh, the computer won. It's ok!")

# Scissors beats Paper

# if (user_choice == "scissors") and (computer_choice == "paper"):
    # print("You win!")

# if (computer_choice == "scissors") and (user_choice == "paper"):
    # print("Oh, the computer won. It's ok!")

# Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

# if (user_choice == "rock") and (computer_choice == "rock"):
    # print("It's a tie!")

# if (user_choice == "paper") and (computer_choice == "paper"):
    # print("It's a tie!")

# if (user_choice == "scissors") and (computer_choice == "scissors"):
    # print("It's a tie!")


# print("Thanks for playing. Please play again!")


# Tie Scenarios - Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"
if user_choice == computer_choice:
    print("It;s a tie, try again!")

# Now, we'll use an elif clause. The way the computer evaluates this is: if the first if condition isn't true, it's going to go to the next elif clause, starting from left to right 
# (Code adapated from Reid in Slack)

if user_choice == "rock":
    if computer_choice == "rock":
        print("IT'S A TIE")
    elif computer_choice == "paper":
        print("OH, THE COMPUTER WON...")
    elif computer_choice == "scissors":
        print("YOU WON! CONGRATS!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("YOU WON! CONGRATS!")
    elif computer_choice == "paper":
        print("IT'S A TIE")
    elif computer_choice == "scissors":
        print("OH, THE COMPUTER WON...")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("OH, THE COMPUTER WON...")
    elif computer_choice == "paper":
        print("YOU WON! CONGRATS!")
    elif computer_choice == "scissors":
        print("IT'S A TIE")

print("Thanks for playing. Please play again!")