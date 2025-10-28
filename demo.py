# demo.py
import operations

def main():
    books = {}
    members = []
    print("Welcome to the Mini Library Management System.")

    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Update Member")
        print("6. Delete Book")
        print("7. Delete Member")
        print("8. Borrow Book")
        print("9. Return Book")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            isbn = input("ISBN: ").strip()
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            genre = input("Genre: ").strip()
            total_copies = input("Total copies: ").strip()
            success, msg = operations.add_book(books, isbn, title, author, genre, int(total_copies))
            print(msg)

        elif choice == '2':
            member_id = input("Member ID: ").strip()
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            success, msg = operations.add_member(members, member_id, name, email)
            print(msg)

        elif choice == '3':
            query = input("Search query (title/author): ").strip()
            results = operations.search_books(books, query)
            if results:
                print("Results:")
                for isbn, book in results:
                    print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}, "
                          f"Genre: {book['genre']}, Available: {book['available_copies']}")
            else:
                print("No books found.")

        elif choice == '4':
            isbn = input("ISBN: ").strip()
            field = input("Field (title/author/genre/total_copies): ").strip()
            value = input("New value: ").strip()
            success, msg = operations.update_book(books, isbn, field, value)
            print(msg)

        elif choice == '5':
            member_id = input("Member ID: ").strip()
            field = input("Field (name/email): ").strip()
            value = input("New value: ").strip()
            success, msg = operations.update_member(members, member_id, field, value)
            print(msg)

        elif choice == '6':
            isbn = input("ISBN: ").strip()
            success, msg = operations.delete_book(books, members, isbn)
            print(msg)

        elif choice == '7':
            member_id = input("Member ID: ").strip()
            success, msg = operations.delete_member(members, books, member_id)
            print(msg)

        elif choice == '8':
            member_id = input("Member ID: ").strip()
            isbn = input("ISBN: ").strip()
            success, msg = operations.borrow_book(books, members, member_id, isbn)
            print(msg)

        elif choice == '9':
            member_id = input("Member ID: ").strip()
            isbn = input("ISBN: ").strip()
            success, msg = operations.return_book(books, members, member_id, isbn)
            print(msg)

        elif choice == '0':
            print("Exiting demo.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()