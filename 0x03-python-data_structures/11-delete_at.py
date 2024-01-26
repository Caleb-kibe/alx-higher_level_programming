#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        list_copy = my_list
        if idx < 0 or idx >= len(list_copy):
            return list_copy
    del list_copy[idx]
    return list_copy
