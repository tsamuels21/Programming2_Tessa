'''
Make a text based version of hangman (25pts)
Use the sample run as an example.  Try to make it as close as possible to the example. (or better)
'''

# PSEUDOCODE
# make a word list for your game
# grab a random word from your list and store it as a variable
# display the hangman
# display the used letters
# display the length of the word to the user using blank spaces
# prompt the user to guess a letter
# if the guess is correct increment correct_guesses by 1
# if the guess is incorrect increment incorrect_guesses by 1 and draw the next part of the hangman
# don't allow the user to select the same letter twice
# if the incorrect_guesses is greater than 6, tell the user they lost and exit the program
# if correct_guesses is equal to the length of the word, tell the user they won
# ask if they want to play again


# Feel free to use this list of ascii art for your game
import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_bank = ["hill", "ordinary", "sound", "seal", "snatch", "whip", "marine", "cottage", "awful", "talkative", "stock",
             "scenario", "explain", "bald", "glance", "deviation", "modernize", "leak", "opinion", "directory",
             "charter", "adult", "overall", "ambiguous", "throw", "discovery", "cotton", "perceive", "grip", "wait",
             "cover", "elephant", "heavy", "spend", "heart", "sunshine", "lot", "mislead", "measure", "shame", "broken",
             "different", "pillow", "swim", "tension", "failure", "credit", "easy", "bow", "nonsense", "beef",
             "appoint", "install", "move", "kettle", "senior", "merchant", "tidy", "rainbow", "courtesy", "brush",
             "fragrant", "fabricate", "muscle", "defend", "bronze", "surprise", "slice", "lay", "holiday", "wind",
             "push", "flavor", "thought", "disappear", "path", "nervous", "past", "academy", "marsh", "fantasy"]

used_letter_list = []

def hang_man():
    correct_guesses = 0
    incorrect_guesses = 0
    play_again = ""
    done = False

    my_word = word_bank.pop(random.randrange(len(word_bank)))

    print("Welcome to Hangman")

    while done is False:
        print(HANGMANPICS[incorrect_guesses])

        print("Used Letters: ", end=" ")

        for i in range(len(used_letter_list)):
            used = used_letter_list[i]

            print(used, end=" ")

        print()
        print()

        for letter in my_word:
            if letter in used_letter_list:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        print()
        print()
        letter = input("Choose your letter: ")

        letter = letter.lower()

        if letter in used_letter_list:
            print("You have already used that letter")
        else:
            used_letter_list.append(letter)

        if letter in my_word:
            correct_guesses += 1
        else:
            incorrect_guesses += 1

        print()

        if correct_guesses == len(my_word):
            print("You Won!!!")
            play_again = input("Would You like to play again?")

        if incorrect_guesses >= 6:
            print(HANGMANPICS[incorrect_guesses])
            print("You Lost :(")
            print("Your word was ", my_word)
            play_again = input("Would You like to play again?")

        if play_again.lower() == "yes" or play_again.lower() == "y":
            hang_man()

        if play_again.lower() == "no" or play_again.lower() == "n":
            print("Thank you for playing Hangman")
            done = True


hang_man()

