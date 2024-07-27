#Write a Python program that prints the numbers from 1 to 10 using a for loop and the range function.

for n in range(10):
    print(n+1)
#Write a Python program that prints the even numbers from 2 to 20 using a for loop and the range function.
for x in range(2, 21, 2):
    print(x)

#Write a Python program that prints the squares of numbers from 1 to 10 using a for loop and the range function.
for n in range(11):
    print(n**2)

#EXTRA CHALLENGE. Write a Python program that prints only the odd numbers from 3 to 21 using a for loop and the range function.
for y in range(3, 22, 2):
    print(y)

#Write a program that prints 10 squares of 4 stars each using a for loop inside a for loop
for s in range(10):
    for n in range(4):
        print("*" * 4)
    print("")

