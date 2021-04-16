# -*- coding: utf-8 -*-

"""
Doc: show how to use it

$ python readFile.py data.txt

Show content of data.txt
"""

import sys

if __name__ == "__main__":
    with open(sys.argv[1],'r',encoding = 'utf8') as f:
        # indicates that the second argument in terminal is to be used
        for line in f:
            print(line[:-1])