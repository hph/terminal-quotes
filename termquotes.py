#!/us/bin/env python
#coding=cp861

from random import choice

files = ['icelandic.txt', 'general.txt']

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
            # Comment, ignore the line.
            continue
        elif line[0] == '[' and line[-2] == ']':
            # Line contains the name of the author.
            author = line[1:-2]
            continue
        elif line == '&\n' or line == '\n' or index == len:
            # Ampersand: detect another quote by the same author.
            # Newline: detect new quote or end of quotes by the same author.
            temp_quotes.append(''.join(lines))
            lines = []
            if line == '\n' or index == len:
                # Finish adding the quotes to the list.
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
        quotes.update(parse(file))
    author = choice([key for key in quotes for value in quotes[key]])
    quote = choice(quotes[author])
    print '\n%s\n\t~%s\n' % (quote, author)

if __name__ == '__main__':
    main()
