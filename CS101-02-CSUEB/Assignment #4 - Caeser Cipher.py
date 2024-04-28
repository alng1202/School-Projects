"""
Alan Nguyen
sj5778
"""

print("Caesar Cipher Program\n")

while True:
    mode = input("Would you like to encrypt, or decrypt?: ")
    
    if mode.lower() == "encrypt":
        encryptShift = int(input("What is the number of shifts used for encrypting?: "))
        message = input("What message would you like to encrypt?: ")
        encryptMessage = ""
        for i in message:
            if (ord(i) >= ord("a") and ord(i) <= ord("z")) or (ord(i) >= ord("A") and ord(i) <= ord("Z")):
                #checks if letter is uppercase
                if i.isupper():
                    #if uppercase, then encrypt letter according to ASCII A-Z
                    encryptMessage += chr((ord(i) + encryptShift - 65) % 26 + 65)
                else:
                    #if lowercase, then encrypt letter according to ASCII a-z
                    encryptMessage += chr((ord(i) + encryptShift - 97) % 26 + 97)
            else:
                encryptMessage += i
        print("\nYour message: " + message)
        print("Your encrypted message: " + encryptMessage)
        
        tryAgain = input("\nRun again? (yes or no): ").lower()
        
        if tryAgain == "yes":
            print("\n")
            continue
        elif tryAgain == "no":
            print("Ok then...")
            break
        else:
            print("Error. Code ending.")
            break
        #if the user inputs are invalid, then code either asks user to correct themselves, or accept that they're intentionally getting it wrong
    elif mode.lower() == "decrypt":
        encryptShift = int(input("What is the number of shifts used for encrypting?: "))
        message = input("What message would you like to decrypt?: ")
        decryptMessage = ""
        for i in message:
            if (ord(i) >= ord("a") and ord(i) <= ord("z")) or (ord(i) >= ord("A") and ord(i) <= ord("Z")):
                #checks if letter is uppercase
                if i.isupper():
                    #if uppercase, then encrypt letter according to ASCII A-Z
                    decryptMessage += chr((ord(i) - encryptShift - 65) % 26 + 65)
                else:
                    #if lowercase, then encrypt letter according to ASCII a-z
                    decryptMessage += chr((ord(i) - encryptShift - 97) % 26 + 97)
            else:
                decryptMessage += i
        print("\nYour message: " + message)
        print("Your decrypted message: " + decryptMessage)

        tryAgain = input("\nRun again? (yes or no): ").lower()
        
        if tryAgain == "yes":
            print("\n")
            continue
        elif tryAgain == "no":
            print("Ok then...")
            break
        else:
            print("Error. Code ending.")
            break
    elif input("Invalid input. Run again? (yes or no): ").lower() == "yes":
        pass
    else:
        print("Ok then...")
        break
    #if the user inputs are invalid, then code either asks user to correct themselves, or accept that they're intentionally getting it wrong
