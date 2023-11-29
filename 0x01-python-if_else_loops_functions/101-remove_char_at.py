#!/usr/bin/python3
def remove_char_at(str, n):
    list = []
    count = 0
    for i in str:
        list.append(i)
    if n in range(len(str)):
        list.remove(list[n])
    return ''.join(list)
