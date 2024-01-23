#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return None
    replaced_list = my_list[idx]
    my_list[idx] = element

    return replaced_list
