#!/usr/bin/python3
import calculator_1 as cal
from sys import argv

if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print(f"{a} + {b} = {cal.add(a, b)}")
        elif argv[2] == "-":
            print(f"{a} - {b} = {cal.sub(a, b)}")
        elif argv[2] == "*":
            print(f"{a} * {b} = {cal.mul(a, b)}")
        else:
            print(f"{a} / {b} = {cal.div(a, b)}")
