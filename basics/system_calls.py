#!/usr/bin/python3

__author__ = "Anon0nyx"

import os
from subprocess import call

# Using the os interface to access system information
print(os.getcwd())
print(os.getuid())
print(os.getenv("PATH"))

# Using systems
os.system("ls -la")
inp = input("Hit Enter")
call(["screenfetch"])
