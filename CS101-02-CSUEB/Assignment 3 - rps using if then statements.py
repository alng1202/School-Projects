# Alan Nguyen
# sj5778
# PROVIDED CODE
# The following code is provided for your use
# Do not make any changes to it or remove
# See the example below to understand how to use
# this example function.
import random
def rpsChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
# End of provided code
## EXAMPLE CODE
## You may use this as an example.
## Comment out or remove
"""
answer = input("Would you like to see what the computer would choose? yes or no? ")
if answer.lower() == 'yes':
    print("The computer chose " + rpsChoice())
else:
    print("Ok..")
"""
## End of example code
## Your code goes here

print("Rock Paper Scissors Game")

playerType = input("Play against a friend or the Computer? Enter F or C: ").lower()
#asks user who they want to play with, then run corresponding loop
if playerType == "c":
    playerTwo = input("Enter name for Player 2: ")
    playerTwoChoice = input(playerTwo + " choose Rock, Paper, or Scissors: ")
    computerChoice = rpsChoice()
    #assign return value of rpsChoice() to variable computerChoice
    #define computer and player variables to compare
    if playerTwoChoice.lower() == "rock":
        if computerChoice == "rock":
            print("\nComputer chose " + computerChoice)
            print(playerTwo + " chose " + playerTwoChoice + "\n")
            print("Tie Game!")
        if computerChoice == "paper":
            print("\nComputer chose " + computerChoice)
            print(playerTwo + " chose " + playerTwoChoice + "\n")
            print("Computer Wins!")
        if computerChoice == "scissors":
            print("\nComputer chose " + computerChoice)
            print(playerTwo + " chose " + playerTwoChoice + "\n")
            print(playerTwo + " Wins!")
    elif playerTwoChoice.lower() == "paper":
        if computerChoice == "paper":
            print("\nComputer chose " + computerChoice)
            print(playerTwo + " chose " + playerTwoChoice + "\n")
            print("Tie Game!")
        if computerChoice == "scissors":
            print("\nComputer chose " + computerChoice)
            print(playerTwo + " chose " + playerTwoChoice + "\n")
            print("Computer Wins!")
        if computerChoice == "rock":
            print("\nComputer chose " + computerChoice)
            print(playerTwo + " chose " + playerTwoChoice + "\n")
            print(playerTwo + " Wins!")
    elif playerTwoChoice.lower() == "scissors":
        if computerChoice == "scissors":
            print("\nComputer chose " + computerChoice)
            print(playerTwo + " chose " + playerTwoChoice + "\n")
            print("Tie Game!")
        if computerChoice == "rock":
            print("\nComputer chose " + computerChoice)
            print(playerTwo + " chose " + playerTwoChoice + "\n")
            print("Computer Wins!")
        if computerChoice == "paper":
            print("\nComputer chose " + computerChoice)
            print(playerTwo + " chose " + playerTwoChoice + "\n")
            print(playerTwo + " Wins!")
    #the code compares the user's answer with the computer's answer, then runs the corresponding loop
else:
    if playerType == "f":
        playerOne = input("Enter name for Player 1: ")
        playerTwo = input("Enter name for Player 2: ")
        playerOneChoice = input(playerOne + " chose Rock, Paper, or Scissors: ")
        playerTwoChoice = input(playerTwo + " chose Rock, Paper, or Scissors: ")
        #define two player variables to compare
        if playerTwoChoice.lower() == "rock":
            if playerOneChoice == "rock":
                print("\n" + playerOne + " chose " + playerOneChoice)
                print(playerTwo + " chose " + playerTwoChoice + "\n")
                print("Tie Game!")
            if playerOneChoice == "paper":
                print("\n" + playerOne + " chose " + playerOneChoice)
                print(playerTwo + " chose " + playerTwoChoice + "\n")
                print(playerOne + " Wins!")
            if playerOneChoice == "scissors":
                print("\n" + playerOne + " chose " + playerOneChoice)
                print(playerTwo + " chose " + playerTwoChoice + "\n")
                print(playerTwo + " Wins!")
        elif playerTwoChoice.lower() == "paper":
            if playerOneChoice == "paper":
                print("\n" + playerOne + " chose " + playerOneChoice)
                print(playerTwo + " chose " + playerTwoChoice + "\n")
                print("Tie Game!")
            if playerOneChoice == "scissors":
                print("\n" + playerOne + " chose " + playerOneChoice)
                print(playerTwo + " chose " + playerTwoChoice + "\n")
                print(playerOne + " Wins!")
            if playerOneChoice == "rock":
                print("\n" + playerOne + " chose " + playerOneChoice)
                print(playerTwo + " chose " + playerTwoChoice + "\n")
                print(playerTwo + " Wins!")
        elif playerTwoChoice.lower() == "scissors":
            if playerOneChoice == "scissors":
                print("\n" + playerOne + " chose " + playerOneChoice)
                print(playerTwo + " chose " + playerTwoChoice + "\n")
                print("Tie Game!")
            if playerOneChoice == "rock":
                print("\n" + playerOne + " chose " + playerOneChoice)
                print(playerTwo + " chose " + playerTwoChoice + "\n")
                print(playerOne + " Wins!")
            if playerOneChoice == "paper":
                print("\n" + playerOne + " chose " + playerOneChoice)
                print(playerTwo + " chose " + playerTwoChoice + "\n")
                print(playerTwo + " Wins!")
    #the code compares both player's choice, then runs the corresponding loop
