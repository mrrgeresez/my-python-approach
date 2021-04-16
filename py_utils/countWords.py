# -*- coding: utf-8 -*-

"""
    Count number of words of text file
    $ python countWords.py data

"""

import sys

if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        w = 0 # counter
        for line in f:
            words = line.split()
            w += len(words)
        print(w)
