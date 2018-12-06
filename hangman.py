# HANGMAN by Taylor meyer
# Last edit: 10/10/2018

from sys import exit
import secrets

####################################################################
def displayMan(attempt):
    print("")
    print("")# Indents to visually separate each run
    print("")
    # Eight attempts until player loses
    if attempt == 0: # Platform shown by default
        print ("  ")
        print ("  ")
        print ("  ")
        print ("  ")
        print ("  ")
        print ("  ")
        print (" ############")
    elif attempt == 1: # Post
        print (" |------")
        print (" |")
        print (" |")
        print (" |")
        print (" |")
        print (" |")
        print (" ############")
    elif attempt == 2: # Head
        print (" |------")
        print (" |")
        print (" |     O")
        print (" |")
        print (" |")
        print (" |")
        print (" ############")
    elif attempt == 3: # Body
        print (" |------")
        print (" |")
        print (" |     O")
        print (" |     |")
        print (" |")
        print (" |")
        print (" ############")
    elif attempt == 4: # One arm
        print (" |------")
        print (" |")
        print (" |    \O")
        print (" |     |")
        print (" |")
        print (" |")
        print (" ############")
    elif attempt == 5: # Both arms
        print (" |------")
        print (" |")
        print (" |    \O/")
        print (" |     |")
        print (" |")
        print (" |")
        print (" ############")
    elif attempt == 6: # One leg
        print (" |------")
        print (" |")
        print (" |    \O/")
        print (" |     |")
        print (" |    /")
        print (" |")
        print (" ############")
    elif attempt == 7: # Both legs
        print (" |------")
        print (" |")
        print (" |    \O/")
        print (" |     |")
        print (" |    / \\")
        print (" |")
        print (" ############")
    elif attempt == 8: # Noose (death)
        print (" |------")
        print (" |     |")
        print (" |    \O/")
        print (" |     |")
        print (" |    / \\")
        print (" |")
        print (" ############")
        print ("  YOU LOSE!")
        exit(0)
    else:
        print ("ERROR displayMan()")
####################################################################
# Open txt file of 849 words
file = open("words.txt", "r")

# Create array of each word terminated by \n
words = file.read().splitlines()

# Generate random index [0,849)
index = secrets.randbelow(849)

# Get the word
word = words[index]

# Debug mode
#print("                WORD = ", word)
#

# Make the word a list of characters
wordL = []
for i in word:
    wordL.append(i)

# Create string of blank spaces
spaces = []
for x in range(0,len(word)):
    spaces.append("-")

# Declare alphabet
alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

# Declare used letters string
used = []
for i in range(0,26):
    used.append('-')

count = 0
while True: # The logic will exit loop if it is a win or loss
    # If the game was a loss (8 attempts gone and word not guessed):
    #   print what the word was a the hanged-man
    if count == 8:
        print("")
        print("The word was:", word)
        displayMan(count)
    else:
    # If an attempt remains:
        displayMan(count)# Display the man
        count += 1 # Increment the attempts
        print("")

        # Print the empty spaces for the word,
        #   and fill in letters that were chosen
        for j in spaces: 
            print(j, end="")
        print("")
        
        for j in alphabet: # Print the alphabet
            print(j, end="")
        print("")
        
        for j in used: # Print string of used characters
            print(j, end="")
        print("")

        # Ask for next character
        character = input("Enter charcter: ")

        # Check if the guessed letter is in the word
        index = -1
        for j in wordL:
            index += 1
            if j == character:
                spaces[index] = j
                # Take back the miss
                count -= 1

        # Mark the letter as having been guessed
        for j in range(len(alphabet)):
            if alphabet[j] == character:
                used[j] = character
                break

        # If the word as been found
        if spaces == wordL:
            print("")
            print("")
            print("")
            print("Answer:", word)
            print("YOU WIN!")
            exit(0)
            
