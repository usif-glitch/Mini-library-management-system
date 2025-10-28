# Mini-library-management-system
my assignment
Library Management System (Python)
--------------------------------------------------------

This project is a simple Library Management System built in Python using lists, dictionaries, tuples, and functions.
It allows users to add, search, update, delete, borrow, and return books while managing library members.

--------------------------------------------------------
Features
--------------------------------------------------------
- Add / Update / Delete Books
- Add / Update / Delete Members
- Search Books by title or author
- Borrow Books (up to 3 per member)
- Return Books
- Data Validation (unique ISBNs, valid genres, available copies)
- Unit Tests and Demo Script included

--------------------------------------------------------
Project Structure
--------------------------------------------------------
LibraryManagementSystem/
│
├── operations.py      # Core functions (add, search, update, delete, borrow, return)
├── demo.py            # Runs the main program (user interaction)
├── tests.py           # Unit tests using assert
├── UML.png / UML.pdf  # Hand-drawn UML or flowchart diagram
├── DesignRationale.pdf# Explanation of data structure choice
└── README.txt         # Instructions to run the project

--------------------------------------------------------
Requirements
--------------------------------------------------------
- Python 3.8+
- No external libraries required (uses built-in Python modules only)

--------------------------------------------------------
How to Run the Code
--------------------------------------------------------
1. Clone or Download the Project
   git clone https://github.com/yourusername/LibraryManagementSystem.git
   cd LibraryManagementSystem

2. Run the Demo Script
   python demo.py

--------------------------------------------------------
Running the Unit Tests
--------------------------------------------------------
python tests.py

Expected Output:
All tests passed successfully!

--------------------------------------------------------
Example Interaction (demo.py)
--------------------------------------------------------
===== LIBRARY MENU =====
1. Add Book
2. Add Member
3. Search Books
4. Update Book
5. Update Member
6. Delete Book
7. Delete Member
8. Borrow Book
9. Return Book
10. Exit
========================
Enter choice: 1

Enter ISBN: 1234
Enter title: Python Basics
Enter author: John Doe
Enter genre: Fiction
Enter total copies: 3
Book added successfully!

--------------------------------------------------------
Design Overview
--------------------------------------------------------
- Dictionaries: Used for books (ISBN → book details) since ISBNs are unique keys.
- Lists: Used for members because the collection is unordered and supports multiple entries.
- Tuples: Used for genres since they are fixed and immutable.
- Functions: Promote modularity, reusability, and readability.

--------------------------------------------------------
Documentation
--------------------------------------------------------
- DesignRationale.pdf — explains why specific data structures were used.
- UML.png / Flowchart.png — visual representation of data flow and function interactions.

--------------------------------------------------------
Example Test Cases (in tests.py)
--------------------------------------------------------
assert add_book('1234', 'Python 101', 'John Doe', 'Fiction', 2) == True
assert add_book('1234', 'Duplicate', 'Jane', 'Fiction', 1) == False
assert borrow_book('M001', '1234') == True
assert borrow_book('M001', '1234') == True
assert borrow_book('M001', '1234') == False  # No copies left
assert return_book('M001', '1234') == True

--------------------------------------------------------
Author
--------------------------------------------------------
Esther Mamie Sowa
Intermediate Python Developer
Library Management System (Python)
--------------------------------------------------------

This project is a simple Library Management System built in Python using lists, dictionaries, tuples, and functions.
It allows users to add, search, update, delete, borrow, and return books while managing library members.

--------------------------------------------------------
Features
--------------------------------------------------------
- Add / Update / Delete Books
- Add / Update / Delete Members
- Search Books by title or author
- Borrow Books (up to 3 per member)
- Return Books
- Data Validation (unique ISBNs, valid genres, available copies)
- Unit Tests and Demo Script included

--------------------------------------------------------
Project Structure
--------------------------------------------------------
LibraryManagementSystem/
│
├── operations.py      # Core functions (add, search, update, delete, borrow, return)
├── demo.py            # Runs the main program (user interaction)
├── tests.py           # Unit tests using assert
├── UML.png / UML.pdf  # Hand-drawn UML or flowchart diagram
├── DesignRationale.pdf# Explanation of data structure choice
└── README.txt         # Instructions to run the project

--------------------------------------------------------
Requirements
--------------------------------------------------------
- Python 3.8+
- No external libraries required (uses built-in Python modules only)

--------------------------------------------------------
How to Run the Code
--------------------------------------------------------
1. Clone or Download the Project
   git clone https://github.com/yourusername/LibraryManagementSystem.git
   cd LibraryManagementSystem

2. Run the Demo Script
   python demo.py

--------------------------------------------------------
Running the Unit Tests
--------------------------------------------------------
python tests.py

Expected Output:
All tests passed successfully!

--------------------------------------------------------
Example Interaction (demo.py)
--------------------------------------------------------
===== LIBRARY MENU =====
1. Add Book
2. Add Member
3. Search Books
4. Update Book
5. Update Member
6. Delete Book
7. Delete Member
8. Borrow Book
9. Return Book
10. Exit
========================
Enter choice: 1

Enter ISBN: 1234
Enter title: Python Basics
Enter author: John Doe
Enter genre: Fiction
Enter total copies: 3
Book added successfully!

--------------------------------------------------------
Design Overview
--------------------------------------------------------
- Dictionaries: Used for books (ISBN → book details) since ISBNs are unique keys.
- Lists: Used for members because the collection is unordered and supports multiple entries.
- Tuples: Used for genres since they are fixed and immutable.
- Functions: Promote modularity, reusability, and readability.

--------------------------------------------------------
Documentation
--------------------------------------------------------
- DesignRationale.pdf — explains why specific data structures were used.
- UML.png / Flowchart.png — visual representation of data flow and function interactions.

--------------------------------------------------------
Example Test Cases (in tests.py)
--------------------------------------------------------
assert add_book('1234', 'Python 101', 'John Doe', 'Fiction', 2) == True
assert add_book('1234', 'Duplicate', 'Jane', 'Fiction', 1) == False
assert borrow_book('M001', '1234') == True
assert borrow_book('M001', '1234') == True
assert borrow_book('M001', '1234') == False  # No copies left
assert return_book('M001', '1234') == True

--------------------------------------------------------
Author
--------------------------------------------------------
Esther Mamie Sowa
Intermediate Python Developer
