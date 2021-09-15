!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    keys = []
    if a_dictionary:
        for k, i in a_dictionary.items():
            keys.append(k)

        keys.sort()
        for k in keys:
            print("{}: {}".format(k, a_dictionary[k]))
