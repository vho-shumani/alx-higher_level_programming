#!/usr/bin/python3
def uppercase(str):
	for i in str:
		print("{}".format(i if ord(i) not in range(97, 123) else chr(ord(i) - 32)), end="")
	print("{}".format("\n"),end="")
