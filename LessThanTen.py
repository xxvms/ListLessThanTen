#!/usr/bin/python3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def selection_function(user_d):
    less_then = []
    for i in a:
        if i < int(user_d):
            less_then.append(i)
        else:
            continue
    print(less_then)


userDigit = input("Print smaller numbers than: ")
selection_function(userDigit)


