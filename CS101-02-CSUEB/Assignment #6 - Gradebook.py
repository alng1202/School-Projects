def getName():
###########################
#   Your code here        #
###########################
    name = input("What is your name? ")
    # return user input (their name)
    while name == "":
        name = input("What is your name? ")
    return name

def getScore():
###########################
#   Your code here        #
###########################
    # return user input (their grade)
    while True:
        try:
            score = float(input("Enter student's score: "))
            if score < 0:
                print("Write a positive float.")
                continue
            break
        except ValueError:
            print("Write a positive float.")
    return score

def newScore():
###########################
#   Your code here        #
###########################
    ## opens the text file in 'append' mode
    records = open('records.txt', 'a')

    ## calls getName, then append user input, in lowercase, into records.txt
    records.write(getName().lower() + '\n')

    ## calls getScore, then append user input, in lowercase, into records.txt
    records.write(str(getScore()) + '\n')

    ## close file after finishing
    records.close()
    
    print("The name and score saved.")
    
def readRecords():
###########################
#   Your code here        #
###########################

    ## opens text file in 'read' mode
    records = open('records.txt', 'r')

    ## assign contents in records to variable
    record_contents = records.read()

    ## close records file
    records.close()
    
    print(record_contents)

def getGrade(studentName):
###########################
#   Your code here        #
###########################
    ## input validation for studentName
    while studentName == "":
        studentName = input("Enter the student name: ")
        
    ## asks user for total points
    ## input validation
    while True:
        try:
            totalPoints = float(input("Enter total points: "))
            if totalPoints < 0:
                print("Write a positive float.")
                continue
            break
        except ValueError:
            print("Write a positive float.")

    ## create variable to add total points in records
    total = 0

    ## open records file in 'read' mode
    records = open('records.txt', 'r')

    ## assign first line in 'records.txt' to search variable
    search = records.readline()

    ## if the file hits an empty line, break code
    ## whenever search hits a line/name they want to find the grade for, go to next line, turn value to float, then add to total
    ## return grade
    while search != "":
        search = search.rstrip('\n')
        if search == studentName.lower():
            search = records.readline()
            total += float(search)
            search = records.readline()
        else:
            search = records.readline()
            search = records.readline()
    records.close()

    finalGrade = round((total/totalPoints) * 100, 2)
    return str(finalGrade) + "%"

def menu():
    response = ""
    while response.lower() != "exit":
        print("\n\nWelcome to the grade book")
        print("Choose one of the following: ")
        print("Enter a new test score: <NEW>")
        print("Read all scores: <READ>")
        print("Get Student grade: <GRADE>")
        response = input(" :: ")
        if response.lower() == "read":
            readRecords()
        elif response.lower() == "new":
            newScore()
        elif response.lower() == "grade":
            name = input("Enter the student name: ")
            score = getGrade(name)
            print(name + " overall score is " + str(score))
        elif response.lower() != "exit":
            print("Invalid response")

def main():
    menu()
    print("Thank you for using the gradebook")

main()
