#Exercise about List

#You're managing a small library of books. You need to perform several operations to update your collection and prepare a display list for a thematic book week.

list_of_Books = ["The Great Gatsby","To Kill a Mockingbird", "1984", "Moby-Dick", "War and Peace"]

#1 Create and print the list of books.
print(list_of_Books)

#2 Access and print the third book in the list.
print(list_of_Books[2])

#3 Slice and print the first three books.
print(list_of_Books[:3])

#4 Concatenate a new list of books with the existing one and print the result. New books: "Pride and Prejudice", "The Catcher in the Rye".
new_books = ["Pride and Prejudice", "The Catcher in the Rye"]
new_list= list_of_Books + new_books
print(new_list)

#5 Repeat the list of all books twice and print the result.
print(new_list *2)

#6 Modify the list: Change "1984" to "Brave New World".
new_list[2] = "Brave New World"
print(new_list)

#7 Add "The Hobbit" to the end of the list.
new_list.append("The Hobbit")
print(new_list)

#8 Insert "Harry Potter" at the beginning of the list.
new_list.insert(0, "Harry Potter")
print(new_list)

#9 Remove "Moby-Dick" from the list.
new_list.remove("Moby-Dick")
print(new_list)

# 10 Delete the second book in the list.
del new_list[1]
print(new_list)

#11 Pop the last book from the list and print its title.
text = new_list.pop()
print(text)

#12 Check if "The Great Gatsby" is in the list and print the result.
print("The Great Gatsby" in new_list)

#13 Print the final list of books.
print(new_list)