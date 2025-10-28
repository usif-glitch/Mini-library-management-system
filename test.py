# tests.py
# Unit tests using assert

import operations

def test_add_book_success():
    books = {}
    success, msg = operations.add_book(books, '123', 'Test Book', 'Test Author', 'Fiction', 5)
    assert success == True
    assert 'Test Book' in books['123']['title']
    assert books['123']['available_copies'] == 5

def test_add_book_invalid_genre():
    books = {}
    success, _ = operations.add_book(books, '123', 'Test', 'Author', 'Invalid', 1)
    assert success == False

def test_add_book_duplicate_isbn():
    books = {'123': {}}
    success, _ = operations.add_book(books, '123', 'Test', 'Author', 'Fiction', 1)
    assert success == False

def test_add_member_success():
    members = []
    success, _ = operations.add_member(members, 'M001', 'John Doe', 'john@example.com')
    assert success == True
    assert len(members) == 1
    assert members[0]['borrowed'] == []

def test_add_member_duplicate_id():
    members = [{'id': 'M001'}]
    success, _ = operations.add_member(members, 'M001', 'John', 'john@example.com')
    assert success == False

def test_search_books():
    books = {
        '123': {'title': 'Python Basics', 'author': 'Jane Smith'},
        '456': {'title': 'Advanced Python', 'author': 'Bob Johnson'}
    }
    results = operations.search_books(books, 'Python')
    assert len(results) == 2
    results = operations.search_books(books, 'Jane')
    assert len(results) == 1

def test_borrow_book_success():
    books = {'123': {'available_copies': 1}}
    members = [{'id': 'M001', 'borrowed': []}]
    success, _ = operations.borrow_book(books, members, 'M001', '123')
    assert success == True
    assert len(members[0]['borrowed']) == 1
    assert books['123']['available_copies'] == 0

def test_borrow_book_no_copies():
    books = {'123': {'available_copies': 0}}
    members = [{'id': 'M001', 'borrowed': []}]
    success, _ = operations.borrow_book(books, members, 'M001', '123')
    assert success == False

def test_borrow_book_max_books():
    books = {'123': {'available_copies': 1}}
    members = [{'id': 'M001', 'borrowed': ['456', '789']}]
    success, _ = operations.borrow_book(books, members, 'M001', '123')
    assert success == False

def test_return_book_success():
    books = {'123': {'available_copies': 0}}
    members = [{'id': 'M001', 'borrowed': ['123']}]
    success, _ = operations.return_book(books, members, 'M001', '123')
    assert success == True
    assert len(members[0]['borrowed']) == 0
    assert books['123']['available_copies'] == 1

def test_delete_book_with_borrows():
    books = {'123': {}}
    members = [{'borrowed': ['123']}]
    success, _ = operations.delete_book(books, members, '123')
    assert success == False

def test_delete_member_with_borrows():
    members = [{'id': 'M001', 'borrowed': ['123']}]
    books = {}
    success, _ = operations.delete_member(members, books, 'M001')
    assert success == False

def test_update_book_total_copies():
    books = {'123': {'total_copies': 5, 'available_copies': 3}}
    success, _ = operations.update_book(books, '123', 'total_copies', '2')
    assert success == True
    assert books['123']['available_copies'] == 2  # min(3,2)=2

if __name__ == "__main__":
    test_add_book_success()
    test_add_book_invalid_genre()
    test_add_book_duplicate_isbn()
    test_add_member_success()
    test_add_member_duplicate_id()
    test_search_books()
    test_borrow_book_success()
    test_borrow_book_no_copies()
    test_borrow_book_max_books()
    test_return_book_success()
    test_delete_book_with_borrows()
    test_delete_member_with_borrows()
    test_update_book_total_copies()
    print("All tests passed!")