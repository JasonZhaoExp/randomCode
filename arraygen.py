# arraygen.py

from Crypto.Random import random

def generate_random_sequenced_array(min_num=0, max_num=1024):
    array = [a for a in range(min_num, max_num)]
    return array_randomizer(array)

def generate_random_array(size=1024, min_num=0, max_num=1024):
    array = []
    for i in range(size):
        array.append(random.randint(min_num, max_num))
    return array

def array_randomizer(array = [a for a in range(1, 1024)]):
    return random.shuffle(array)