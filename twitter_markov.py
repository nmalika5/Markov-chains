from random import choice
import sys

import os
import twitter

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )

def tweet_markov(chains):

    print api.VerifyCredentials()

    status = api.PostUpdate(make_text(chains))
    print status.text

def tweet_normally(post):
     api.PostUpdate(post[:140])

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    file_data = open(file_path).read()


    return file_data
    

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
    words = text_string.rstrip().replace("\n", " ").split(" ")
    words = [word for word in words if word]
    # can also use: words = filter(None,words)
    
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

    capitalized_keys = [t for t in chains if t[0][0].isupper()]

    random_key = choice(capitalized_keys)
    for word in random_key:
        text += word + " "
    
    writing = True
    while writing:
        next_word = choice(chains[random_key])

        if text + next_word > 140:
            writing = False

        text += next_word + " "

        if any(p in next_word for p in ('.','!','?','--')):
            writing = False

        next_key = [word for word in random_key[1:]]
        next_key.append(next_word)

        random_key = tuple(next_key)

        if random_key not in chains:
            writing = False

    return text

def combine_files(list):
    combined_data = ''
    for item in list:
        combined_data += open_and_read_file(item) + " "

    return combined_data

def print_last_tweet(user):
    print (api.GetUserTimeline(user)[0]).text


twitter_app_running = True

while twitter_app_running:
    user_choice = raw_input("What would you like to do? Enter \'t\' to tweet normally, \
\'m\' to tweet a markov text, \'g\' to print last tweet, or \'q\' to quit.\n").lower()
    if user_choice == 'm':
        n_grams = int(raw_input("Enter the number of n_grams you want? "))
        input_file = raw_input("Enter the files you'd like to combine, separated by spaces: ").split(" ")
        input_text = combine_files(input_file)
        chains = make_chains(input_text)
        tweet_markov(chains)
    elif user_choice == 't':
        post = raw_input("Type your tweet: ")
        tweet_normally(post)
    elif user_choice == 'g':
        user = raw_input("Enter the username to retreive its last tweet: ")
        print_last_tweet(user)
    elif user_choice == 'q':
        twitter_app_running = False
    else:
        print "Invalid input! Please try again."



# Open the file and turn it into one long string

# Get a Markov chain

# Produce random text
# random_text = make_text(chains)
