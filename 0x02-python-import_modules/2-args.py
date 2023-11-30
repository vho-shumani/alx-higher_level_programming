#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len = len(argv) - 1
    if len != 1:
        print("{} {}".format(len, "arguments:" if len > 1  else "arguments."))
    else:
        print(f"{len} argument:")
    for i in range (1, len + 1):
        print(f"{i}: {argv[i]}")
