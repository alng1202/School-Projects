## Alan Nguyen
## sj5778

## import random library
import random
vowel = ['a', 'e', 'i', 'o', 'u']

## define function endChoice()
## returns one string from the three in the list
def suffixChoice():
    suffix = ['hay', 'way', 'yay']
    return random.choice(suffix)

## define function pigLatin() with one argument: word
## the code returns the word translated to pig latin
## if the word starts with a vowel, call endChoice to choose a suffix
## otherwise return the word translated to pig latin
def pigLatin(word):
    word_length = len(word)
    for char in word:
        word_pos = word.index(char)
        if char in vowel:
            if word_pos == 0:
                return word[word_pos:word_length] + word[0:word_pos] + suffixChoice()
            break
    return word[word_pos:word_length] + word[0:word_pos] + "ay"

## define function line_to_pigLatin() with one arguement: line
## the code returns the sentence in pig latin
def line_to_pigLatin(line):
    pig_latin_sentence = ""
    sentence = line.split()
    for word in sentence:
        pig_latin_sentence += pigLatin(word) + " "
        
    return pig_latin_sentence

## define function write_to_pigLatin_file()
## the code create/overwrite a pigLatin.txt file
## the 'pigLatin.txt' file contains the pig latin version of the provided 'word.txt' file
def write_to_pigLatin_file():
    word_file = open('words.txt', 'r')
    pigLatin_file = open('pigLatin.txt', 'w')

    line = word_file.readline()

    while line != "":
            pigLatin_file.write(line_to_pigLatin(line) + "\n")
            line = word_file.readline()
            
    word_file.close()
    pigLatin_file.close()

## define function main()
## main calling function to run the translation code
def main():
    write_to_pigLatin_file()
    print("The text file has been translated.")

## Call main() to run program
main()
