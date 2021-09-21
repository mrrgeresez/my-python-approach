# Reminder:
# to run script on python console use: run script_name args
# to run script on OS terminal use: python (or python3) script_name.py args

import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y") # object creation and description (-h)
group = parser.add_mutually_exclusive_group() # add mutually exclusive arg
group.add_argument("-v", "--verbose", action="store_true") # optional arguments have two names
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base") # positional arguments, order matter if there are more than one
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args() # method to return data
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")