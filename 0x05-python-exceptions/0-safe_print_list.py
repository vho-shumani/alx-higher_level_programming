def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for x in range(0, x):
            print(my_list[x], end='')
            i += 1
    except IndexError:
        pass
    print()
    return i
