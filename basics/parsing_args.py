#!/usr/bin/python3

__author__ = 'Anon0nyx'

import argparse

parser = argparse.ArgumentParser(description='type: python3 parsing_args.py -i *var* (optional) -o *var*')
parser.add_argument('-i', type=str, help='This is a required variable', required=True)
parser.add_argument('-o', type=str, help='This is optional', required=False)

# cmdargs ends up being a dictionary/hash
cmdargs = parser.parse_args()

# Access the parameter based on the flag
ivar = cmdargs.i 
print(ivar)
ivar = cmdargs.o
print(ivar)