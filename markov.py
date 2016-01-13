from random import choice
import sys
from string import *

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    file_data = open(file_path).read()


    return file_data


n_grams = int(raw_input("Enter the number of n_grams you want? "))
    

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    words = text_string.rstrip().replace("\n"," ").split(" ")
    
    indicies = range(len(words)-n_grams)

    for i in indicies:    
        key = tuple([words[i] for i in range(i,n_grams+i)])
        next_word = words[i+1]

        if key not in chains:
            chains[key] = []
        chains[key].append(next_word)

    return chains 



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    capitalized_keys = []

    for t in chains:
        if t[0][0][0].isupper():
            capitalized_keys.append(t)

    print capitalized_keys
    chosen_word = choice(capitalized_keys)
    
    for word in chosen_word:
        text += word + " "
    
# break this function into two for readability

    writing = True

    while writing:
        next_word = choice(chains[chosen_word])

        text += next_word + " "
        next_key = []

        for word in chosen_word:
            next_key.append(word)

        next_key.append(next_word)
        chosen_word = tuple(next_key[1:])

        if chosen_word not in chains:
            writing = False



    return text
    # slice text at punctuation

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
