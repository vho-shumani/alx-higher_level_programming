#!/usr/bin/python3
def best_score(a_dictionary):
    biggest_score = ""
    num = 0
    if not a_dictionary:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > num:
            biggest_score = i
            num = a_dictionary[i]
    return biggest_score

