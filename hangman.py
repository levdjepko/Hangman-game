#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
choice = random.randint(0, 2)
pickedWord = word_list[choice]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letterGuessedByUser = input("Pick a letter: ")


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in pickedWord:
    if (letterGuessedByUser == letter):
        print ("Right")
    else:
        print ("Wrong")    
