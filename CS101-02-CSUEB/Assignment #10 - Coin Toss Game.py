## import 'random' library
import random
## list of choices for the classes to refer to
choices = ["heads", "tails"]

## create Coin() class
## contains contructor, toss method, get_sideup method
## simulates the toss of a singular coin
class Coin:
    ## constructor contains 1 private variable
    def __init__(self):
        self.__side_up = random.choice(choices)

    ## siimulate coin toss
    def toss(self):
        self.__side_up = random.choice(choices)

    ## returns the side of the coin facing up
    def get_sideup(self):
        return self.__side_up

## create Game() class
## contains constructor, play method, and get_winner method
## simulates a coin toss game
class Game:
    ## constructor contains 3 private variables
    ## takes the names of player 1 and 2
    ## calls play() method to start the game
    def __init__(self):
        self.__coin = Coin().get_sideup()
        
        print("\nIMPORTANT:")
        print("Player 1 will always choose first.")
        print("Player 2 will automatically pick the remaining option.")
        
        self.__p1name = input("\nWhat is player 1's name?: ")
        self.__p2name = input("What is player 2's name?: ")
        self.__winner = self.play()

    ## play method
    ## asks player 1 to choose heads or tails
    ## assigns output to private winner variable
    def play(self):
        print(f"\n{self.__p1name}'s choice: <HEADS> or <TAILS>")
        p1choice = input(" :: ").lower()

        ## input validation
        ## code loops when user types singular head/tail
        ## or anything else other than the provided choices
        while True:
            try:
                if p1choice[-1] != "s":
                    p1choice += "s"
                    
                    if p1choice not in choices:
                        print("\nInvalid input: <HEADS> or <TAILS>")
                        p1choice = input(" :: ").lower()
                    else:
                        break
                else:
                    break
            except IndexError:
                print("\nInvalid input: <HEADS> or <TAILS>")
                p1choice = input(" :: ").lower()

        ## after all conditions met, assign heads/tails
        if p1choice == "heads":
            p2choice = "tails"
        else:
            p2choice = "heads"
            
        print(f"\n{self.__p2name}'s choice will be {p2choice}.")

        ## choose winner
        if self.__coin == p1choice:
            self.__winner = self.__p1name
        else:
            self.__winner = self.__p2name

        ## call get_winner() to print winner
        self.get_winner()
    ## method get_winner
    ## when called, prints the winner
    def get_winner(self):
        print(f"\nThe coin shows {self.__coin}. {self.__winner} wins!")

## define menu() function
## when called, game menu loads and asks user to play or exit
def menu():
    print("Welcome to the coin toss game!")
    print("To play, correctly guess which side of the coin is facing up and you will win!")
    print("\nChoose one of the following: ")
    print("Play game: <PLAY>")
    print("Exit game: <EXIT>")
    play = input(" :: " ).lower()
    
    while play != "exit":
        if play != "play":
            print("Invalid input.")
            print("\nChoose one of the following: ")
            print("Play game: <PLAY>")
            print("Exit game: <EXIT>")
            play = input(" :: " ).lower()
        else:
            Game()
            print("Thank you for playing!")
            print("\nChoose one of the following: ")
            print("Play game: <PLAY>")
            print("Exit game: <EXIT>")
            play = input(" :: " ).lower()
    print("\nGame ended. Thank you for playing.")

## run menu() to run code
menu()
