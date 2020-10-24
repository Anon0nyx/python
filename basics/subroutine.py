#!/usr/bin/python3

__author__ = "Anon0nyx"

def sub(x, y):
    # out of scope here
    z = x - y
    print(z)

def add(x, y):
    return x + y

print(add(15,4))

sub(15, 4)
