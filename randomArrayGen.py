# randomArrayGen.py

from Crypto.Random import random

def generate_random_array(size=1024, min_num=0, max_num=1024):
    array = []
    for i in range (size):
        array.append(random.randint(min_num, max_num))
    return array

def array_randomizer(array = [a for a in range(1, 1024)]):
    array_copy = array
    for i in range(len(array)):
        array[i] = random.choice(array_copy)