#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if element < 0 and element >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
