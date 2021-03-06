import os
import sys
from random import choice
import twitter

# api = twitter.Api(
#     consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
#     consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
#     access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
#     access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])


def open_and_read_file(filenames):
    """Given a list of files, open them, read the text, and return one long
        string."""

    body = ""

    for filename in filenames:
        text_file = open(filename)
        body = body + text_file.read()
        text_file.close()

    # print body

    return body


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains."""

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

        # or we could replace the last three lines with:
        #    chains.setdefault(key, []).append(value)

    # print "TEXT make_chains" 
    # print chains
    return chains

def make_text(chains):

#Alternative for checking the length of the string option 2
# def make_text(chains, limit=140):
    """Takes dictionary of markov chains; returns random text."""
    # print chains
    key = choice(chains.keys())
    markov_chain = key[0] + key[1]

    # Alternative for checking the length of the string option 2 
    # while key in chains and len(markov_chain) <= limit:
    while key in chains:

        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text)
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

        word = choice(chains[key])
        # sum_words = sum([len(i) for i in words])
        # if sum_words <= 140:
          
        markov_chain = markov_chain + " " + word 
        
        key = (key[1], word)

    # if len(markov_chain) <= 140:
    return markov_chain
    # print "TEXT of words:"
    # print markov_chain

    # return " ".join(words)

    # return chains

    # return markov_chain


# def tweet(chains):
    # Use Python os.environ to get at environmental variables
    # Note: you must run `source secrets.sh` before running this file
    # to make sure these environmental variables are set.

def tweet(markov_chain):

    # pseudocode:
        # call make_text function to find 140 random words from the dictionary chains
        # then prompt for user to tweet again or quit 
        
    # OPTION 1 for modifying the length of string to be less than 140 characters
    markov_chain = markov_chain[:140]
    # print tweet

    api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    print api.VerifyCredentials()

    status = api.PostUpdate(markov_chain)

    print status.text


    return 

    # response = raw_input("Type 'enter' to tweet again or 'q' to quit] > ")
   
    # while response != 'q':
    #     tweet(markov_chain)
    
    
    # else:

    # pass
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get the filenames from the user through a command line prompt, ex:
# python markov.py green-eggs.txt shakespeare.txt
while True:

    response = raw_input("Continue typing 'enter' to tweet or 'q' to quit > ")

    if response != 'q':

        filenames = sys.argv[1:]

        # Open the files and turn them into one long string
        text = open_and_read_file(filenames)

        chain = make_chains(text)

        # Get a Markov chain
        markov_chain = make_text(chain)

        #tweet(markov_chain)

        tweet(markov_chain)
    else:
        break
# else:
#     pass
    # loop through functions for new markov_chain and then tweet 

# Your task is to write a new function tweet, that will take chains as input
# tweet(chains)
