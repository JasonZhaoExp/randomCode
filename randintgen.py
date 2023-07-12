# randintgen.py

from Crypto.Random import random
import sys

args = sys.argv
lowerlimit = int(sys.argv[1])
upperlimit = int(sys.argv[2])
numOfNums = 1
try:
    numOfNums = int(sys.argv[3])
except:
    pass

for i in range(numOfNums):
    print(random.randint(lowerlimit, upperlimit))