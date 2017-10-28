"""
This python module provides solution for Chapter 1 - Unit 5 - One Away
"""
import unittest
LEN = 256
#chr(i) is inbuilt python function that returns unicode character representing the integer i
MIN_CHARACTER = chr(0)

def one_away(string_a, string_b):
    """
    This function takes two strings as input.
    This function checks if they are 1 or 0 edits away
    """
    len1 = len(string_a)
    len2 = len(string_b)
    if len1 > len2 + 1 or len2 > len1 + 1:
        return False
    #This array stores the count of characters for string_a
    arr_a = [int(0) for i in range(0, LEN +1)]
    for char_iterator in string_a:
        temp_var = ord(char_iterator) - ord(MIN_CHARACTER)
        arr_a[temp_var] = arr_a[temp_var] + 1
    # Now will check if number of edits are more than 1
    edits_allowed = 1
    for char_iterator in string_b:
        temp_var = ord(char_iterator) - ord(MIN_CHARACTER)
        arr_a[temp_var] = arr_a[temp_var] - 1
        if arr_a[temp_var] < 0:
            if edits_allowed < 1:
                return False
            else:
                edits_allowed = edits_allowed - 1
    return True

print(one_away("pile", "piles"))
