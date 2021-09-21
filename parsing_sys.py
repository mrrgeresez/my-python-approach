# Reminder:
# to run script on python console use: run script_name args
# to run script on OS terminal use: python (or python3) script_name.py args

# Display numbers and sum

import sys

print("This is the name of the script: ", sys.argv[0]) # 0 is the script name
print("Number of arguments (including script name): ", len(sys.argv))
print("The arguments are: \n")
n = len(sys.argv)
for i in range(1, n):
    print(sys.argv[i], end = " ")
Sum = 0
for i in range(1, n):
    Sum += int(sys.argv[i])
print("\ntotal sum:", Sum)

