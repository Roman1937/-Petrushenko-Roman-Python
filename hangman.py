# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random

import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    if set(secret_word) == set(letters_guessed):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    s = secret_word
    g_word = "_ " * len(secret_word)
    l1 = list()
    for i in letters_guessed:
        n = s.count(i)
        for j in range(n):
            g_word = list(g_word)
            g_word[2 * (s.index(i))] = i
            l1.append(2 * (s.index(i)))
            s = list(s)
            s[s.index(i)] = "*"
            s = "".join(s)

    l1.sort()
    c = 0
    if len(l1) == 1:
        g_word.pop(l1[0] + 1)
    while c < len(l1) - 1:
        if l1[c + 1] == l1[c] + 2:
            g_word[l1[c] + 1] = "-"
            g_word[l1[c] + 3] = "-"
        c += 1
    g_word = "".join(g_word)
    g_word = g_word.replace("-", "")
    return g_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman(secret_word):
    len_s = len(secret_word)
    n_warnings = 3
    n_guesses = 6
    l_guessed = []
    l_guessed1 = []
    a_letters = string.ascii_lowercase
    print(f"""Welcome to the game Hangman!
I am thinking of a word that is {len_s} letters long.
You have {n_warnings} warnings left.
""")
    while True:
        print("-----------")
        if set(secret_word) == set(l_guessed1):
            print(f"Congratulations, you won! Your total score for this game is: {len(set(secret_word)) * n_guesses}")
            break
        if n_guesses <= 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            break
        print(f"You have {n_guesses} guesses left.")
        print(f"Available letters: {a_letters}")
        a = input("Please guess a letter: ").lower()
        if a.isalpha() == False or len(a) != 1:
            if n_warnings > 0:
                n_warnings -= 1
                print(f"Oops! That is not a valid letter. You have {n_warnings} warnings left: {get_guessed_word(secret_word, l_guessed)}")
            else:
                n_guesses -= 1
                print(f"""Oops! That is not a valid letter. You have no warnings left 
so you lose one guess: {get_guessed_word(secret_word, l_guessed)}""")
            continue

        elif a in l_guessed:
            if n_warnings > 0:
                n_warnings -= 1
                print(
                    f"Oops! You've already guessed that letter. You have {n_warnings} warnings left: {get_guessed_word(secret_word, l_guessed)}")
            else:
                n_guesses -= 1
                print(f"""Oops! You've already guessed that letter. You have {n_warnings} warnings left            "
so you lose one guess: {get_guessed_word(secret_word, l_guessed)} """)
        else:
            l_guessed.append(a)
            if a in secret_word:
                l_guessed1.append(a)
                print(f"Good guess: {get_guessed_word(secret_word, l_guessed)}")
            elif a not in secret_word:
                if a in "aeiou":
                    n_guesses -= 2
                else:
                    n_guesses -= 1
                print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, l_guessed)}")
            a_letters = a_letters.replace(a, "")

#hangman("abrakadabra")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    t = 0
    ow_gaps = list()
    for i in my_word:
        if i != "_":
            ow_gaps.append(other_word[t])
        else:
            ow_gaps.append("_")
        t += 1
    ow_gaps = "".join(ow_gaps)
    if my_word == ow_gaps:
        return True
    else:
        return False

def show_possible_matches(my_word):
    print("Possible word matches are: ",end="")
    for j1 in wordlist:
            if match_with_gaps(my_word, j1) == True:
                print(j1,end = " ")
    print(" ")


def hangman_with_hints(secret_word):
    len_s = len(secret_word)
    n_warnings = 3
    n_guesses = 6
    l_guessed = []
    l_guessed1 = []
    a_letters = string.ascii_lowercase
    print(f"""Welcome to the game Hangman!
I am thinking of a word that is {len_s} letters long.
You have {n_warnings} warnings left.
""")
    while True:
        print("-----------")
        if set(secret_word) == set(l_guessed1):
            print(f"Congratulations, you won! Your total score for this game is: {len(set(secret_word)) * n_guesses}")
            break
        if n_guesses <= 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            break
        print(f"You have {n_guesses} guesses left.")
        print(f"Available letters: {a_letters}")
        a = input("Please guess a letter: ").lower()
        if a == "*" and len(l_guessed1) !=0 :
            show_possible_matches(get_guessed_word(secret_word, l_guessed))
            continue
        if a == "*" and len(l_guessed1) == 0 :
            print(f"Possible word matches are: {wordlist}")
            continue


        if a != "*" and a.isalpha() == False or len(a) != 1:
            if n_warnings > 0:
                n_warnings -= 1
                print(f"Oops! That is not a valid letter. You have {n_warnings} warnings left: {get_guessed_word(secret_word, l_guessed)}")
            else:
                n_guesses -= 1
                print(f"""Oops! That is not a valid letter. You have no warnings left 
so you lose one guess: {get_guessed_word(secret_word, l_guessed)}""")
            continue

        if a in l_guessed:
            if n_warnings > 0:
                n_warnings -= 1
                print(f"Oops! You've already guessed that letter. You have {n_warnings} warnings left: {get_guessed_word(secret_word, l_guessed)}")
            else:
                n_guesses -= 1
                print(f"""Oops! You've already guessed that letter. You have {n_warnings} warnings left            "
so you lose one guess: {get_guessed_word(secret_word, l_guessed)} """)
            continue
        else:
            l_guessed.append(a)
            if a in secret_word:
                l_guessed1.append(a)
                print(f"Good guess: {get_guessed_word(secret_word, l_guessed)}")
            elif a not in secret_word:
                if a in "aeiou":
                    n_guesses -=2
                else:
                    n_guesses -= 1
                print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, l_guessed)}")
            a_letters = a_letters.replace(a, "")

#hangman_with_hints(banana)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman(secret_word)



# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
