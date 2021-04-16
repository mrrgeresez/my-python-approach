# -*- coding: utf-8 -*-

"""
    $ python copyBinary.py source copy
    copy source to copy name

"""

import sys

if __name__ == "__main__":
    with open(sys.argv[1],'rb') as f:
        with open(sys.argv[2],'wb') as g:
            for line in f:
                g.write(line)