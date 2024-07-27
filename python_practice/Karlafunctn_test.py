# Create a function greet that receives a name as an argument and prints "Hello, [name]!".
# Use a for loop to call the function with the names "Alice", "Bob", and "Charlie".
def hi(names):
    for name in names:
        print(f"Hello {name}")


nams = ["Alice", "Bob", "Charlie"]
hi(nams)


# Create a function is_even that receives a number as an argument and prints True if the number is even,
# and False otherwise. Use a for loop to call the function with the numbers 1 to 10.
# Print the result of each call.
def is_even(num):
    if num % 2 == 0:
        print(f"{num} True")
    else:
        print(f"{num} False")


for number in range(0, 11):
    is_even(number)

print("_____________")

# Create a function is_odd that receives a number as an argument and prints True if the number
# is odd, and False otherwise. Use a for loop to call the function with the numbers 1 to 10.
# Print the result of each call.
def is_odd(num):
    if num % 2 == 1:
        print(f"{num} True")
    else:
        print(f"{num} False")


for number in range(1, 11):
    is_odd(number)

# Create a function has_more_than_5_characters that receives a string as an argument and
# prints True if the string has more than 5 characters, and False otherwise.
# Use a for loop to call the function with the names "Alice", "Bob", and "Charlie".
# Print the result of each call.

def has_more_than_5_characters(string):
    if len(string) > 5:
        print(f"{string} True")
    else:
        print(f"{string} False")
for string in ["Ami", "Vishal", "Sushma", "Karla", "Sushiii"]:
    has_more_than_5_characters(string)
