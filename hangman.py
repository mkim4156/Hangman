
from random import choice, random

dictionary_file = "dictionary_short.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12
def import_dictionary (filename) :
    dictionary = {}
    l3, l4, l5, l6, l7, l8, l9, l10, l11, l12 = [], [], [], [], [], [], [], [], [], []
    try:
        with open(filename) as fn:
            file_size = len(fn.readlines())
            fn.seek(0)
            for i in range(file_size):
                content = fn.readline().upper()
                match len(content.strip()):
                    case 3:
                        dictionary[3] = l3
                        l3.append(content.strip())
                    case 4:
                        dictionary[4] = l4
                        l4.append(content.strip())
                    case 5:
                        dictionary[5] = l5
                        l5.append(content.strip())
                    case 6:
                        dictionary[6] = l6
                        l6.append(content.strip())
                    case 7:
                        dictionary[7] = l7
                        l7.append(content.strip())
                    case 8:
                        dictionary[8] = l8
                        l8.append(content.strip())
                    case 9:
                        dictionary[9] = l9
                        l9.append(content.strip())
                    case 10:
                        dictionary[10] = l10
                        l10.append(content.strip())
                    case 11:
                        dictionary[11] = l11
                        l11.append(content.strip())
                    case 12:
                        dictionary[12] = l12
                        l12.append(content.strip())
    except IOError:
        print("Could not read file:", filename)
    return dictionary


# print the dictionary (use only for debugging)
def print_dictionary(dictionary):
    max_size = 12
    print(dictionary)


# get options size and lives from the user, use try-except statements for wrong input
def get_game_options():
    size, lives = 0, 0
    print("Please choose a size of a word to be guessed [3 - 12, default any size]: ", end="")
    try:
        size = int(input('\n'))
        if size < 3 or size > 12:
            size = choice(range(3, 13))

    except ValueError:
        size = choice(range(3, 13))
        print("", end="")

    print("The word size is set to", str(size) + ".")

    print("Please choose a number of lives [1 - 10, default 5]: ", end="")
    try:
        lives = int(input('\n') or 5)
        if lives < 1 or lives > 10:
            lives = 5

    except ValueError:
        lives = 5
    print("You have", lives, "lives.")

    return (size, lives)


# MAIN

if __name__ == '__main__' :
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    # remove after debugging the dictionary function import_dictionary
    ###print_dictionary(dictionary)
    # print a game introduction
    print("Welcome to the Hangman Game!")

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    play_again = "Y"
    while play_again == "Y":
        #getting size and lives
        size, lives = get_game_options()

        #saving X's and O's
        current_lives = []
        for i in range(lives):
            current_lives.append("O")

        #retrieving the random word based on the size user have inputed
        word = choice(dictionary.get(size))

        # set up game options (the word size and number of lives)
        #list that saves chosen letters
        word_history = []
        index = 0
        updated_lives = lives
        user_input = ""
        #using the word length as to make a template for the user to see and save the correct input to display to user.
        word_character = []
        for i in range(len(word)):
            word_character.append("__")
        while True:
            #Printing out the letters have been chosen from the user
            print("Letters chosen: ", end="")
            for i in range(len(word_history)):
                if i == len(word_history) - 1:
                    print(word_history[i], end="")
                    continue
                print(word_history[i] + ", ", end="")
            print()

            for i in range(len(word_character)):

                #condition if the word match "-"
                if word[i] == "-":
                    word_character[i] = "-"
                    print(word_character[i], " ", end="")
                    continue

                #condition if the word match.
                if word[i] == user_input:
                    word_character[i] = user_input
                    print(word_character[i], " ", end="")
                    continue

                print(word_character[i], " ", end="")

            print(" lives:", updated_lives, "", end="")

            #Displaying lives of X's and O's
            for i in range(lives):
                print(current_lives[i], end="")
            print()

            #winning and losing condition
            if "__" not in word_character:
                print("Congratulations!!! You won! The word is", word + "!")
                break
            elif updated_lives == 0:
                print("You lost! The word is", word + "!")
                break
            else:
                while True:
                    try:
                        print("Please choose a new letter > ")
                        user_input = input().upper()
                        if len(user_input) != 1 or not user_input.isalpha():
                            print("", end="")
                        else:
                            break
                    except ValueError:
                        print("", end="")

                if user_input in word_history:
                    print("You have already chosen this letter.")
                    while True:
                        print("Please choose a new letter >")
                        try:
                            user_input = input().upper()
                            if len(user_input) != 1 or not user_input.isalpha():
                                print("", end="")
                            elif user_input in word_history:
                                print("", end="")
                            else:
                                break
                        except ValueError:
                            print("", end="")

            #Condition to add only words that are not currently added into the list.
            if user_input not in word_history:
                word_history.append(user_input)

            #Condition to check if the word the user enter are in the current word list.
            #If not, then decrementing the user lives and incrementing the index for the next life to lose
            #And replacing with O with X.
            if user_input not in word:
                print("You guessed wrong, you lost one life.")
                current_lives[index] = "X"
                updated_lives = updated_lives - 1
                index = index + 1
            else:
                print("You guessed right!")

        #End Inner While loop

        #Asking the user if they want to play it again.
        #If no, then breaks the while loops
        print("Would you like to play again [Y/N]? ", end="")
        play_again = input('\n').upper()

    #Outter loop end.
    print("Goodbye!")
    #Program End
