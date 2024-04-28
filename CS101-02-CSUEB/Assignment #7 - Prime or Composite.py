## Alan Nguyen
## sj5778

## Code by Prof. Christopher Smith
## requires 1 argument, n: the max for the loop
## loop starts at 2, stops at n
## if prime number, return True
## if composite number, return False
def prime_or_composite(n):
    has_divisor = False    
    for i in range(2, n):
        if n % i == 0:
            has_divisor = True
    if has_divisor:
        return False
    else:
        return True

## define append_list function with one argument: userNum
## call function prime_or_composite for conditional
## using a for loop,
    ## if prime_or_composite returns True, append number i to prime list, then print
    ## if False, append number i to composite list, then print
def append_list(userNum):
    for i in range(2, userNum + 1):
        if prime_or_composite(i) == True:
            prime.append(i)
            print("Prime: " + str(i))
        else:
            composite.append(i)
            print("Composite: " + str(i))

## define write_to_prime_file function
## if prime.txt doesnt exist, create new file
## if prime.txt exists, overwrite file
## using for loop, write new entry into prime.txt file
## close file
def write_to_prime_file():
    primeFile = open('prime.txt', 'w')
    for num in prime:
        primeFile.write(str(num) + '\n')
    primeFile.close()
    
## define write_to_composite_file function
## if composite.txt doesnt exist, create new file
## if composite.txt exists, overwrite file
## using for loop, write new entry into composite.txt file
## close file
def write_to_composite_file():
    compositeFile = open('composite.txt', 'w')
    for num in composite:
        compositeFile.write(str(num) + '\n')
    compositeFile.close()

## define functions to read prime.txt and composite.txt
## commented due to not being necessary
## made to check if file entries are valid and code is working as intended
"""
def read_prime_file():
    primeFile = open('prime.txt', 'r')
    print(primeFile.read())
    primeFile.close()

def read_composite_file():
    compositeFile = open('composite.txt', 'r')
    print(compositeFile.read())
    compositeFile.close()
"""
## define main function
## user input validation
## validates input for userNum to pass into append_list function
## if userNum is not a number greater than 1, asks the user for another number
## Value exception error
## once userNum is defined correctly, call append_list and pass userNum as argument
## once append_list is finished running, call write_to_prime_file and write_to_composite file
def main():
    while True:
        try:
            userNum = int(input("Pick a number to identify as prime or composite: "))
            if userNum < 2:
                print("Please input a valid integer.")
                continue
            break
        except ValueError:
            print("Please input a valid integer.")
    append_list(userNum)
    
    write_to_prime_file()
    write_to_composite_file()

## define list prime
## define list composite
## call main function
prime = []
composite = []
main()
