library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

# TODO - Print welcome statement including library name
print(f"Welcome to the {library['name']}. Use this service to find and edit books in the catalogue.")

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")

    if option == "1":
        print("Listing all books...")
        # TODO - List all books
        for book in library["books"]:
            print(book)
        print()                                                                     # I just want a line break here so it's not so crowded.

    if option == "2":
        print("Searching for a book by title...")
        # TODO - Search for a book by title
        book_to_search = input("Title: ")
        available_books = library["books"]
        found = False
        for book in available_books:
            if book_to_search.lower() == book["title"].lower():                     # in case they write in lowercase
                found = True
                print(f"{book['title']} is available for checkout.")
        if found == False:
            print(f"There is no book in the catalogue with the title '{book_to_search}'.")
        print()

    if option == "3":
        print("Adding a book...")
        # TODO - Add a book
        new_author = input("Author: ")
        new_title = input("Title: ")
        library["books"].append({"author": new_author, "title": new_title})
        print(f"{new_title} has been added to the catalogue.")
        print()

    if option == "4":
        print("Removing a book...")
        # TODO - Remove a book
        book_to_remove = input("Title: ")
        available_books = library["books"]
        found = False
        for book in available_books:
            if book_to_remove.lower() == book["title"].lower():
                found = True
                available_books.remove(book)
                print(f"{book['title']} has been removed from the catalogue.")
        if found == False:
            print(f"There is no book in the catalogue with the title '{book_to_remove}'.")
        print()

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book
        book_to_update = input("Title: ")
        available_books = library["books"]
        found = False
        for book in available_books:
            if book_to_update.lower() == book["title"].lower():
                found = True
                updated_author = input("New author: ")
                updated_title = input("New title: ")
                if updated_author == "" or updated_title == "":
                    print(f"{book['title']} was not updated. A new title and author must be given.")
                else:
                    book["author"] = updated_author
                    book["title"] = updated_title
                    print(f"{book['title']} has been updated.")
        if found == False:
            print(f"There is no book in the catalogue with the title '{book_to_update}'.")
        print()