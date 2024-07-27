# Write a function which_is_longer that accepts two strings for arguments.
#   The function should print out the string that is the longer of the two -
#  that is, whichever has the more characters.
# If the strings are of equal length, the program should print out "The strings are equally long".


def which_is_longer(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str2) > len(str1):
        return str2
    else:
        return "The strings are equally long"


x = input("The 1st string is:")
y = input("The 2nd string is:")
print(which_is_longer(x, y))
