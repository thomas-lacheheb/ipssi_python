#!/usr/bin/python3

import sys

def moyenne(a, b):
    result=(a+b)/2
    return result

avg = moyenne(int(sys.argv[1]), int(sys.argv[2]))
print("la moyenne est :", avg)
