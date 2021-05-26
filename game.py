
import random

print("Rock, Paper, Scissors, Shoot!")

#user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

user_choice = input("Welcome 'Player One' to my Rock-Paper-Scissors game...Please choose either 'rock', 'paper', or 'scissors': ")

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

# Rock beats Scissors

if (user_choice == "rock") and (computer_choice == "scissors"):
    print("You win!")

if (computer_choice == "rock") and (user_choice == "scissors"):
    print("Oh, the computer won. It's ok!")

#Paper beats Rock

if (user_choice == "paper") and (computer_choice == "rock"):
    print("You win!")

if (computer_choice == "paper") and (user_choice == "rock"):
    print("Oh, the computer won. It's ok!")

# Scissors beats Paper

if (user_choice == "scissors") and (computer_choice == "paper"):
    print("You win!")

if (computer_choice == "scissors") and (user_choice == "paper"):
    print("Oh, the computer won. It's ok!")

# Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

if (user_choice == "rock") and (computer_choice == "rock"):
    print("It's a tie!")

if (user_choice == "paper") and (computer_choice == "paper"):
    print("It's a tie!")

if (user_choice == "scissors") and (computer_choice == "scissors"):
    print("It's a tie!")


print("Thanks for playing. Please play again!")