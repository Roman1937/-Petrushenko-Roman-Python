# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
#import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    #print("  ", len(wordlist), "words loaded.")
    return wordlist
words_list = load_words()
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
"""def get_word_score(word, n):
    word = word.lower()
    scores = {"AIOULNSTR": 1, "DG": 2, "ВСMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
    score1 = 0
    for i in word.upper():
        for j in scores.keys():
            if i in j:
               score1 += scores[j]
    score2 = max(1, 7 * len(word) - 3 * (n - len(word)))
    score = score1 * score2
    return score"""
def get_word_score(word, n):
    scores = {"aioulnstr": 1, "dg": 2, "bcmp": 3, "fhvwy": 4, "k": 5, "jx": 8, "qz": 10}
    score1 = 0
    for i in word.lower().replace("*",""):
        for j in scores.keys():
            if i in j:
               score1 += scores[j]
    score2 = max(1, 7 * len(word) - 3 * (n - len(word)))
    score = score1 * score2
    return score













    


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"] = 1

    for i in range(n-(num_vowels+1)):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    hand1 = hand.copy()
    for i in word.lower():
        if i in hand1.keys():
            hand1[i] -=1
    hand2 = hand1.copy()
    for j in hand1.keys():
        if hand1[j]<=0:
            hand2.pop(j)
    return hand2





#
# Problem #3: Test word validity
#
"""def is_valid_word(word, hand, word_list):
    word = word.lower()
    print(get_frequency_dict(word))
    for i in get_frequency_dict(word).keys():
        if i != "*":
           if i not in hand.keys():
               return False

           elif get_frequency_dict(word)[i] > hand[i]:
               return False

    word_list2 = list()
    for i in word_list:
        if len(i) == len(word):
            word_list2.append(i)


    if "*" in word:
        for i in word_list2:
            i1 = list(i)
            i1[word.index("*")] = "*"
            i1 = "".join(i1)
            word_list2[word_list2.index(i)] = i1

    if word in word_list2:
        return True
    elif word not in word_list2:
        return False"""

def is_valid_word(word, hand, word_list):
    word = word.lower()
    for i in get_frequency_dict(word).keys():
        if i not in hand.keys():

            return False
        elif i != "*" and get_frequency_dict(word)[i] > hand[i]:

            return False

    word_list2 = list()
    for i in word_list:
        if len(i) == len(word):
            word_list2.append(i)


    if "*" in word:
        for i in word_list2:
            i1 = list(i)
            i1[word.index("*")] = "*"
            i1 = "".join(i1)
            word_list2[word_list2.index(i)] = i1

    if word in word_list2:
        return True
    elif word not in word_list2:
        return False
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    return len([i for i in hand.keys()])

l1 = list()

def substitute_hand(hand, letter):
    hand2 = dict()
    for i in hand.keys():
        if i != letter:
            hand2[i] = hand[i]
        elif i == letter:
            a1 = VOWELS+CONSONANTS.replace(i,"")
            for i2 in hand.keys():
                a1 = a1.replace(i2,"")

            hand2[random.choice(a1)] = hand [i]
    return hand2

def play_hand(hand, word_list):
    global l1
    total_points = 0
    n_hand = len(hand)
    while True:
        print("Current Hand:", end = " ")
        display_hand(hand)
        if len(l1) == 0:
            k = input("Would you like to substitute a letter? ")
            if k == "yes":
                letter1 = input("Which letter would you like to replace: ")
                hand = substitute_hand(hand, letter1)
                l1.append("a")
                continue

        word = input("Enter word, or “!!” to indicate that you are finished: ")

        if word == "!!":
            print(f"Total score: {total_points} points")
            break


        elif word != "!!" and is_valid_word(word, hand, word_list) == True:
            total_points += get_word_score(word, n_hand)
            print(f"\"{word}\" earned {get_word_score(word, n_hand)} points.Total:{total_points} points")

        elif word != "!!" and is_valid_word(word, hand, word_list) == False:
            print("That is not a valid word. Please choose another word.")

        hand = update_hand(hand, word)
        if calculate_handlen(hand) == 0:
            print(f"Ran out of letters. Total score: {total_points} points")
            break
    return total_points


#print(play_hand({'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1, "s":1,"e":1,"d":1},words_list))
















#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand1(hand, letter):
    hand2 = dict()
    for i in hand.keys():
        if i != letter:
            hand2[i] = hand[i]
        elif i == letter:
            hand2[random.choice(VOWELS+CONSONANTS.replace(i,""))] = hand [i]
    return hand2

    pass  # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    hands_number = int(input("Enter total number of hands: "))
    total_pts = 0
    n1 = 1
    i1 = 0
    while i1 < hands_number:
        a = play_hand(deal_hand(7), word_list)
        if n1 == 1:
            k1 = input("Would you like to replay the hand? ")
            if k1 == "yes":
                n1 -= 1
                continue
        total_pts += a
        print(f"Total score for this hand: {a}")
        i1+=1
    print(f"Total score over all hands: {total_pts}")
    return total_pts



#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
