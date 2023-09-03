#!/usr/bin/python3
import sys



def factorize(num):
    """will generates two factors for a given number"""
    factor_1 = 2
    while (num % factor_1):
        if (factor_1 <= num):
            factor_1 += 1

    factor_2 = num // factor_1
    return (factor_2, factor_1)

if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()

for line in lines:
    num = int(line.rstrip())
    factor_2, factor_1 = factorize(num)
    print(f"{num} = {factor_2} * {factor_1}")
