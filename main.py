"""
Remove All The Marked Elements of a List
Define a method/function that removes from a given array of integers all the values contained in a second array.
"""

def remove_(integer_list, values_list):
    return [item for item in integer_list if item not in values_list]

