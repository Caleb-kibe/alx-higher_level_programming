#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurences of an element by another in a new list
    Args:
        my_list: the initial list
        search: the element to replace in the list
        replace: the new element
    """
    new_list = []

    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    return new_list
