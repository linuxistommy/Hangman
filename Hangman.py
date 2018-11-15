# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()
secretWord = chooseWord(wordlist)

def hangman(secretWord):
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is', len(secretWord), 'letters long.')
    guesses = 8
    lettersGuessed = []

    def getAvailableLetters(lettersGuessed):
        voca = 'abcdefghijklmnopqrstuvwxyz'
        for letter in lettersGuessed:
            if letter not in voca:
                voca = voca
            else:
                voca = voca.replace(letter, '')
        return voca

    def getGuessedWord(secretWord, lettersGuessed):
        output=''
        for num in range(len(secretWord)):
            if secretWord[num] in lettersGuessed:
                output+=secretWord[num]
                output+=' '
            else:
                output+='_ '
        return output
    
    def isWordGuessed(secretWord, lettersGuessed):
        output=''
        for num in range(len(secretWord)):
            if secretWord[num] in lettersGuessed:
                output+=secretWord[num]
            else:
                output+='_ '
        if output == secretWord:
            return True
        else:
            return False

    while guesses > 0:

        print("------------")
        print('You have', guesses,'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ')
        letter = letter.lower()
        
        if letter in secretWord:
            if letter in lettersGuessed:
                lettersGuessed += letter
                print ("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed += letter
                print ('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        else:
            if letter in lettersGuessed:
                print ("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed += letter
                print ("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
                guesses = guesses - 1
        if isWordGuessed(secretWord, lettersGuessed) is True:
            print("------------")
            print ("Congratulations, you won!")
            break
        if guesses == 0:
            print("------------")
            print ("Sorry, you ran out of guesses. The word was", secretWord,".")

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)