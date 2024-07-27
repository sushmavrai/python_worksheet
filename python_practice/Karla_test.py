#Create a list with the numbers from 1 to 10. Use a for loop to print each number in the list.
numbers = list(range(1, 11))
for number in numbers:
    print(number)

#Create a list with the numbers from 1 to 10. Use a for loop to print each number in the list, but only if the number is even.
for number in numbers:
    if number %2 == 0:
        print(f"{number} is Even" )

#Create a list with the numbers from 1 to 10. Use a for loop to print each number in the list, but only if the number is odd.
for number in numbers:
    if number % 3 == 0:
        print(f"{number} is odd" )
#Create a list of 5 names. Use a for loop to print each name in the list.
names = ["Sushma", "A", "Vishal", "Sumit", "Arya", "Dustin"]
for name in names:
    print(name)
print("___________")

#Create a list of 5 names. Use a for loop to print each name in the list, but only if the name starts with the letter "A".
for name in names:
    if name[0]== "A":
        print(name)
print("_____________")
#Create a list of 5 names. Use a for loop to print each name in the list, but only if the name has more than 5 characters.
for name in names:
    if len(name) > 5:
        print(name)
print("_____________")
#Create a list of 5 names. Use a for loop to print each name in the list using uppercase.
for name in names:
    print(name.upper())
print("____________")
#Using a for loop and the range function, write a program that prints “Hello” 100 times.
for r in range (0,100):
    print(f"{r} Hello")
print("____________________")
#Using a for loop and the range function, write a program that prints the numbers from 1 to 100.
for a in range (1,101):
    print(a)