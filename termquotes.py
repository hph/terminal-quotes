#!/usr/bin/env python
#coding=cp861

import os
import sys
from random import choice

# NOTE Use ConfigParser to find quote files.
current_dir = os.path.dirname(sys.argv[0])
files = ['%s/icelandic.txt' % current_dir, '%s/general.txt' % current_dir,
         '%s/movies.txt' % current_dir]

def parse(input_file):
    '''Return quotes from a parsed file.'''
    quotes = {}
    lines = []
    temp_quotes = []
    with open(input_file) as file:
        # Find the length of the the file (in number of lines).
        # Used later to detect EOF. NOTE Find a better and more pythonic way.
        len = sum([1 for line in file])
    file = open(input_file)
    index = 0
    for line in file:
        index += 1
        if line[0] == '#':
            # The line contains a comment: ignore it.
            continue
        elif line[0] == '[' and line[-2] == ']':
            # Line contains the name of the author.
            author = line[1:-2]
            continue
        elif line == '&\n' or line == '\n' or index == len:
            # Ampersand and newline: add last quote to temp_quotes.
            temp_quotes.append(''.join(lines))
            # Re-initialize temp list (lines).
            lines = []
            if line == '\n' or index == len:
                # Finish adding the quotes to the list if last quote or EOF.
                quotes[author] = temp_quotes
                temp_quotes = []
            continue
        # None of the conditions above were met so the line contains a quote.
        lines.append(line)
    file.close()
    return quotes

def main():
    '''Print a randomly selected quote.'''
    quotes = {}
    for file in files:
        # Update the quotes dictionary with quotes from the chosen files.
        quotes.update(parse(file))
    # Choose an author based on the number of quotes by him (more or less the
    # same probability for all the quotes to appear. NOTE Do it some other way.
    author = choice([key for key in quotes for value in quotes[key]])
    # Select a quote from the author chosen above.
    quote = choice(quotes[author])
    print '\n%s\n\t~ %s\n' % (quote, author)

if __name__ == '__main__':
    main()
