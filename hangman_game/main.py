import random


def display_hangman(attempts):

    stages = [
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]

    print(stages[attempts])


#list of secret words
words=["python","computer","programming","developer","keyboard"]

#select a random word
word=random.choice(words)

#Select guessed letters
guessed_letters = []

#Number of attempts
attempts = 6


print("=======Welcome to hangman ======")


while attempts>0:

    display_hangman(attempts)

    #Display the current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word+= letter + " "
        else:
            display_word+="_ "
    
    print("\nWord:",display_word)
    print("Attempts remaining:",attempts)


    #Checck whether the player won
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations!You Won the Game")
        break


    #Take user input
    guess = input("Guess a letter:").lower()

    #Validate input
    if len(guess) !=1 or not guess.isalpha():
        print("Please enter a single alaphabet")
        continue
    
    #check repeated guesses
    if guess in guessed_letters:
        print("You already guessed the letter")
        continue
    
    guessed_letters.append(guess)


    #check the guess
    if guess in word:
        print("Correct guess")

    else:
        attempts-=1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("The correct word was:",word)

