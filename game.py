print("Rock, Paper, Scissors, Shoot!")

#print(10)
#print(10, 99, "My message", "another message")


user_choice = input("Please choose one of 'rock', 'paper', 'scissors;: ")

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

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN")