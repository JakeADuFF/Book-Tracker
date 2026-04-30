import json
import time
import os
import random

books = []
want_list = []

### Clear Screen ###
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

### New Book ###
def add_new_book(title, author, pages, read_status):
    book = {
        "Title": title,
        "Author": author,
        "Pages": pages,
        "Read Status": read_status
    }
    books.append(book)
    print(f"\n✅ '{title}' added successfully!\n")

### View All Books ###
def view_all_books():
    if not books:
        print("\n⚠️ There are no books in the tracker\n")
        return

    print("\n📚 Your Books: \n")
    for i, book in enumerate(books, 1):
        read_status = "✅ Read" if book["Read Status"] else "❌ Not Read"
        print(f'{i}. {book["Title"]} by {book["Author"]} | {book["Pages"]} pages | {read_status}')
    print()

### Mark a book as read ###
def mark_read(title):
    for book in books:
        if book["Title"].lower() == title.lower():
            book["Read Status"] = True
            print(f"\n✅ '{title}' has been marked as read!\n")
            return
    print(f"\n⚠️ '{title}' not found\n")

### Edit a book ###
def edit_book(title):
    for book in books:
        if book["Title"].lower() == title.lower():
            print(f"\n✏️ Editing '{book['Title']}' (press Enter to keep current value)\n")

            new_title = input(f"New title ({book['Title']}): ") or book["Title"]
            new_author = input(f"New author ({book['Author']}): ") or book["Author"]
            new_pages = input(f"New pages ({book['Pages']}): ") or book["Pages"]

            new_read = input("Have you read this book (yes/no, leave blank to keep current): ").lower()

            if new_read == "":
                new_read_status = book["Read Status"]
            else:
                new_read_status = new_read == "yes"

            book["Title"] = new_title
            book["Author"] = new_author
            book["Pages"] = new_pages
            book["Read Status"] = new_read_status

            print("\n✅ Book updated successfully!\n")
            return

    print(f"\n⚠️ '{title}' not found\n")

### Search For Book ###
def search_book(title):
    found = False
    print("\n🔍 Search Results:\n")
    for book in books:
        if title.lower() in book["Title"].lower():
            read_status = "✅ Read" if book["Read Status"] else "❌ Not Read"
            print(f'{book["Title"]} by {book["Author"]} | {book["Pages"]} pages | {read_status}')
            found = True
    if not found:
        print(f"⚠️ No book found with title containing '{title}'")
    print()

### Remove a book ###
def remove_book(title):
    for book in books:
        if book["Title"].lower() == title.lower():
            books.remove(book)
            print(f"\n🗑️ '{title}' has been removed from your book list\n")
            return
    print(f"\n⚠️ '{title}' not found in your book list\n")

### Remove A Book (Wantlist) ###
def remove_from_want_list(title):
    for book in want_list:
        if book.lower() == title.lower():
            want_list.remove(book)
            print(f"\n🗑️ '{title}' removed from your want list\n")
            return
    print(f"\n⚠️ '{title}' not found in your want list\n")

### Add to wantlist ###
def add_to_want_list(title):
    want_list.append(title)
    print(f"\n✅ '{title}' added to your want list!\n")

### View Wantlist ###
def view_want_list():
    if not want_list:
        print("\n📌 Your want list is empty.\n")
        return

    print("\n📌 Want List:\n")
    for i, book in enumerate(want_list, 1):
        print(f'{i}. {book}')
    print()

### Suggest Random Unread Book ###
def suggest_random_book():
    unread_books = [book for book in books if not book["Read Status"]]
    if unread_books:
        book = random.choice(unread_books)
        print(f"\n📖 Suggested book to read next: {book['Title']} by {book['Author']} ({book['Pages']} pages)\n")
    else:
        print("\n🎉 All books have been read! Add more books to get a suggestion.\n")

### Save Data ###
def save_data():
    data = {
        "books": books,
        "want_list": want_list
    }
    with open("books.json", "w") as file:
        json.dump(data, file, indent=4)
    print("\n💾 Data saved successfully!\n")

### Load Data ###
def load_data():
    global books, want_list
    try:
        with open("books.json", "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                books = data
                want_list = []
            else:
                books = data.get("books", [])
                want_list = data.get("want_list", [])

        print("\n📚 Books loaded successfully!\n")

    except FileNotFoundError:
        print("\n⚠️ No saved books found.\n")

    except json.JSONDecodeError:
        print("\n⚠️ File is empty or corrupted. Starting fresh.\n")
        books = []
        want_list = []

### Menu ###
def menu():
    load_data()

    while True:
        ### Book Menu ###
        clear_screen()
        print("="*40)
        print("        📚 Book Tracker 📚")
        print("="*40)
        print("1. Add a Book")
        print("2. View Books")
        print("3. Mark a Book as Read")
        print("4. Edit a Book")
        print("5. Search for a Book")
        print("6. Remove from Book List")
        print("7. Suggest a Random Unread Book")
        print("8. Save & Exit")

        ### Wantlist menu ###
        print("="*40)
        print("        📌 WantList 📌")
        print("=" * 40)
        print("9. Add to Want List")
        print("10. View Want List")
        print("11. Remove from Want List")
        print("="*40)

        ### Choices ###
        choice = input("Enter your choice: ")

        ### If Choices ###
        if choice == "1":
            title = input("Enter the title: ")
            author = input("Enter the author name: ")
            pages = input("Enter the number of pages: ")
            read_status = input("Have you read this book (yes/no): ").lower() == "yes"
            add_new_book(title, author, pages, read_status)

        elif choice == "2":
            view_all_books()

        elif choice == "3":
            book = input("Which title do you want to mark as read? ")
            mark_read(book)

        elif choice == "4":
            title = input("Enter the title of the book to edit: ")
            edit_book(title)

        elif choice == "5":
            title = input("Enter the title to search: ")
            search_book(title)

        elif choice == "6":
            title = input("Enter the title to remove: ")
            remove_book(title)

        elif choice == "8":
            save_data()
            print("Goodbye!")
            break

        elif choice == "9":
            title = input("Enter the book title to add to want list: ")
            add_to_want_list(title)

        elif choice == "10":
            view_want_list()

        elif choice == "11":
            title = input("Enter the title to remove from want list: ")
            remove_from_want_list(title)

        elif choice == "7":
            suggest_random_book()

        else:
            print("\n⚠️ Invalid choice. Try again\n")

        time.sleep(3)


menu()