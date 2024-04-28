## Alan
## sj5778

## get random choice function
## Takes no arguments
## Returns one of three strings randomly
## To add more choices, add more strings to choices
import random
def getRandomChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

## get choice from user function
## Input validation
## Takes no arguments
## Takes user input and validates against choices
## Returns ONLY one of choice strings
## To add more choices, add more strings to choices
def getChoice():
    choices = ['rock', 'paper', 'scissors']
    userChoice = ""
    while userChoice not in choices:
        userChoice = input("Choose rock, paper, or scissors: ")
    return userChoice.lower()

## get mode function
## Input validation
## Takes no arguments
## Takes user input and validates against choices
## Returns ONLY one of choice strings
## Continue to prompt for choice until user enters a valid answer
## To add more choices, add more strings to choices
def getMode():
    choices = ['friend', 'computer', 'auto']
    ##################
    # YOUR CODE HERE #
    ##################

## asks for user input
## if user input is any different character different than what's in choices, then loop code
## return user input lowercase
    
    modeChoice = ""
    
    while modeChoice not in choices:
        print("Enter play mode:")
        modeChoice = input("<Friend, Computer, or Auto>: ")
    return modeChoice.lower()


## get number function
## Input validation
## Error handling
## returns an int between 0 and max number
## Will not return an unsafe number
## Will not return negative or greater than max number
## Bad user input returns 0
def getNum(max):
    userNumber = input("Enter a number from 0 to " + str(max) + ": ")
    try:
        max = int(max)
        userInt = int(userNumber)
        if userInt > max:
            return max
        elif userInt < 0:
            return 0
        else:
            return userInt

    except ValueError:
        print("Invalid input. Returning zero")
        return 0

## get name function
## Input validation
## takes no arguments
## returns user input string
## Must not allow for a blank name
def getName():
    ##################
    # YOUR CODE HERE #
    ##################
## asks for user input (name)
## if there are no characters in user input, loop code
## returns user input
    name = input("Enter a name for player: ")
    
    while name == "":
        name = input("Enter a name for player: ")
    return name

## get winner function
## Pass in player choices and player names as string arguments
## This function will decide the winner and give output
## Output includes displaying the players names and choices
def getWinner(p1Choice, p2Choice, p1Name, p2Name):
    ##################
    # YOUR CODE HERE #
    ##################

## prints user choices
## compares arguments containing user input with conditions
## if the condition is met, print appropriate output

    print("\n" + p1Name + " chose " + p1Choice)
    print(p2Name + " chose " + p2Choice + "\n")
    
    if p1Choice == "rock":
        if p2Choice == "rock":
            print("Tie Game!")
        elif p2Choice == "paper":
            print(p2Name + " Wins!")
        elif p2Choice == "scissors":
            print(p1Name + " Wins!")
    elif p1Choice == "paper":
        if p2Choice == "rock":
            print(p1Name + " Wins!")
        elif p2Choice == "paper":
            print("Tie Game!")
        elif p2Choice == "scissors":
            print(p2Name + " Wins!")
    elif p1Choice == "scissors":
        if p2Choice == "rock":
            print(p2Name + " Wins!")
        elif p2Choice == "paper":
            print(p1Name + " Wins!")
        elif p2Choice == "scissors":
            print("Tie Game!")
            
## Main function 
## Prints a banner
## Calls the menu function
def main():
    print("Welcome to the Rock Paper Scissors game Version 1.01")
    menu()
    print("End of Main")

## Menu Function
## Loops on the again flag
## Validates input on prompt
## Case insensitive
## Calls play function on "yes" or "y"
## Breaks loop on "no" or "n"
## Output "invalid input" on anything else
def menu():
    ##################
    # YOUR CODE HERE #
    ##################

## asks for user input if they want to play again
## if yes, loop, otherwise pass onto main() function
## if input invalid, print invalid input, then pass to menu function
    
    again = input("Would you like to play? Yes or No ").lower()
    
    if again == "yes" or again == "y":
        play(getMode())
    elif again == "no" or again == "n":
        pass
    else:
        print("invalid input")

# Play function
def play(mode):
    if mode.lower() == "computer":
        p1Name = "Computer"
        p2Name = getName()
        p1Choice = getRandomChoice()
        p2Choice = getChoice()
    elif mode.lower() == "friend":
        p1Name = getName()
        p2Name = getName()
        p1Choice = getChoice()
        p2Choice = getChoice()
    elif mode.lower() == "auto":
        p1Name = "Auto P1"
        p2Name = "Auto P2"
        p1Choice = getRandomChoice()
        p2Choice = getRandomChoice()
    else:
        print("Error")
        return

    getWinner(p1Choice,p2Choice,p1Name,p2Name)
    print("Thank you for playing")
    
# Call main function
main()
