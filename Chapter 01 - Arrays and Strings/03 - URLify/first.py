"""
This python module provides solution for Chapter 1 - Urlify
"""

def urlify(string_a, len_a):
    """
    This function replaces spaces with "%20 character.
    The inserion is in-place as the ample space will be provided at the end of the string.
    True length of string is provided as len_a excluding the spaces at the end
    """
    #character array to store modified string
    list_a = list(string_a)
    # to count number of spaces at the end and save it in variable k
    k = len(string_a) - len_a
    # print(k)
    for i in range(len_a-1, -1, -1):
        if list_a[i] != " ":
            list_a[i+ k] = list_a[i]
        else:
            list_a[i+k] = "0"
            list_a[i+k-1] = "2"
            list_a[i+k-2] = "%"
            k = k-2
    return "".join(list_a)


#to check output
RESULT = urlify("Mr John Smith    ", 13)
print(RESULT)
