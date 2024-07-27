# Write a function underline_print that will get a string argument,
# and then print it “underlined”. The function should print a second line with
# a number of characters equal to the length of the input string. For example,
# underline_print("Hello there!") should print:

def underline_print(str1):
    character = "_"
    x = len(str1)
    i = character * x
    print(str1)
    print(i)
underline_print("Hello There")
