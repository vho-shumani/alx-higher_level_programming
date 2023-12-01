#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_list[idx] = element if 0 <= idx < len(my_list) else my_list
    return my_list

