"""Generate Markov text from text files."""

from asyncio import new_event_loop
from random import choice
from re import L

from pkg_resources import WorkingSet


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    green_eggs = open(input_path).read()

    return green_eggs


def make_chains(green_eggs):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words_list = green_eggs.split()
    for i in range(len(words_list) - 1):
        new_list = []
        key = (words_list[i], words_list[i + 1])
        if not key in chains:
            try:
                new_list.append(words_list[i + 2])
                chains[key] = new_list
            except IndexError:
                pass
        else:
            try:
                new_list = chains[key]
                new_list.append(words_list[i + 2])
                chains[key] = new_list
            except IndexError:
                pass
    print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
