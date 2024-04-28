## create empty wordIndex dictionary
wordIndex = {}

## input validation
## asks for user input for an existing file name
## loops if file isn't found
while True:
    try:
        filename = input("Enter filename for the input: ")
        infile = open(filename,"r")
        break
    except OSError:
        print("Invalid file name. Please input a valid text file.\n")

## defines lines as a line in the text file
lines = infile.readlines()

## all words in the text file will add to wordIndex w/ the words as keys and number of times it shows up as values
for line in lines:
    line = line.rstrip('\n')
    words = line.split()
    for word in words:
        if word in wordIndex:
            wordIndex[word] += 1
        else:
            wordIndex[word] = 1

## define function mostWord()
## finds the most seen word in the text file
def mostWord():
    mostAmount = max(wordIndex.values())
    key_list = list(wordIndex.keys())
    val_list = list(wordIndex.values())
    wordPos = val_list.index(mostAmount)
    word = key_list[wordPos]
    print(f"The most frequent word is '{word}'. It has been seen '{mostAmount}' times.\n")

## define function leastWord()
## finds the least seen word in the text file
def leastWord():
    leastAmount = min(wordIndex.values())
    key_list = list(wordIndex.keys())
    val_list = list(wordIndex.values())
    wordPos = val_list.index(leastAmount)
    word = key_list[wordPos]
    print(f"The least frequent word is '{word}'. It has been seen '{leastAmount}' times.\n")

## define function searchWord
## counts and return user's word choice
def searchWord():
    userWord = ""
    key_list = list(wordIndex.keys())
    val_list = list(wordIndex.values())
    
    while userWord != "cancel":
        userWord = input("What word would you like to search?: ").lower()
        if userWord not in wordIndex:
            print("Word does not exist in file. Please try again, or 'cancel'")
        else:
            wordAmount = wordIndex.get(userWord)
            break

    print(f"The word '{userWord}' been seen '{wordAmount}' times.\n")

## main menu() function
## call menu() to run code
## prompts user what would they like to do with the program
def menu():
    response = ""
    print("\nWelcome to word search!")
    
    while response.lower() != "exit":
        print("Choose one of the following: ")
        print("Search for word: <SEARCH>")
        print("Find most frequently seen words: <MOST>")
        print("Find least frequently seen word: <LEAST>")
        print("EXIT: <EXIT>")
        response = input(" :: ").lower()
        if response == "search":
            searchWord()
        elif response == "most":
            mostWord()
        elif response == "least":
            leastWord()
        elif response != "exit":
            print("Invalid response. Please choose one of the choices, or 'exit'.\n")
            
    print("Program terminated.")
    infile.close()

## run menu() function to start program
menu()
