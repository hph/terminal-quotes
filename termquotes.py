#!/usr/bin/env python
#coding=cp861

import os
import sys
from random import choice

# TODO Use ConfigParser to find quote files instead of this hardcoded crap.
current_dir = os.path.dirname(sys.argv[0])
#files = ['%s/icelandic.txt' % current_dir, '%s/general.txt' % current_dir,
#         '%s/movies.txt' % current_dir]
files = ['%s/icelandic.txt' % current_dir]

file_len = lambda file: sum(1 for _ in open(file))

def parse(input_file):
    '''Return quotes from a parsed file.'''
    quotes = {}
    lines = []
    temp_quotes = []
    len = file_len(input_file)
    # TODO Debug the following code and replace the old one. Raises IndexError.
    # NOTE This code makes the "last-line-empty" requirement (for the quote
    #      files) unnecessary.
    '''
    with open(input_file) as file:
        for line in enumerate(file):
            num, text = line
            if text[0] == '#':
                # The line contains a comment: ignore it.
                continue
            if text[0] == '[' and text[-2] == ']':
                # The line contains the name of an author: add him.
                author = text[1:-2]
                continue
            if num == len:
                if text != '\n':
                    lines.append(text)
            if text in ['&\n', '\n'] or num == len:
                # Ampersand and/or newline: add last quote to temp_quotes.
                temp_quotes.append(''.join(lines))
                # Clear lines for the next quote whether there is one or not.
                lines = []
                if line == '\n' or num == len:
                    # Finish adding the quotes if last quote from author or end
                    # of file.
                    quotes[author] = temp_quotes
                    # Clear temp_quotes lest we're not at the last author.
                    temp_quotes = []
                continue
            # Add the text to lines.
            lines.append(text)
    '''
    file = open(input_file)
    index = 0
    for line in file:
        index += 1
        if line[0] == '#':
            # The line contains a comment - ignore it. No special reason ...
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
    # TODO
    # - Add options and use optparser to allow users to print a quote
    #   on-demand.
    # - Add some kind of formatting options - allow users to select different
    #   settings regarding how the output should be printed.
    # - Write a function to scrape websites for quotes and another to save
    #   them.
    quotes = {}
    for file in files:
        # Load all the quotes.
        quotes.update(parse(file))
    # Choose an author based on the number of quotes by him.
    author = choice([key for key in quotes for value in quotes[key]])
    # Select a quote from the author chosen above.
    quote = choice(quotes[author])
    print '\n%s\n\t~ %s\n' % (quote, author)

if __name__ == '__main__':
    main()
