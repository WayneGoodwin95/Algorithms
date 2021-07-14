"""
computer randomly generates a number between 1 and 15
when you guess the correct number. program ends
"""
from random import *
from math import floor

max = 15
min = 1
rand_num = randint(min, max)

print('LINEAR SEARCH')
# linear search - goes through each iterations one at a time
guesses = 0
guess = 0

while guess != rand_num:
    guess += 1

print('result: {}\n'.format(guess))

print("Binary Search")


def binary_search(rand_num, min, max):
    guesses = 1
    guess = floor(max / 2)
    print(guess)
    while rand_num != guess:

        if guess > rand_num:
            max = guess
            guess = max - floor((max - min) / 2)
        elif guess < rand_num:
            min = guess
            guess = min + floor((max - min) / 2)

        guesses += 1

        print(guess)
    return 'result: {}\n'.format(guesses)


print(binary_search(rand_num, min, max))

new_rand_num = randint(1, 300)

print(binary_search(new_rand_num, 1, 300))

from numpy import sum


def binary_search_primes(primes, num):
    max = len(primes) - 1
    min = 0
    i = floor((min + max) / 2)
    searching = True
    while searching:

        if num > primes[i]:
            min = i
            i = floor((min + max) / 2)
        elif num < primes[i]:
            max = i
            i = floor((min + max) / 2)

        if num == primes[i]:
            return 'is a prime at position {}'.format(i)
        elif max - min == 1:
            return 'Not a Prime'

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
num = 67
print(binary_search_primes(primes, num))

print(binary_search_primes(primes, 42))

