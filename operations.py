# operations.py

GENRES = ('Fiction', 'Non-Fiction', 'Sci-Fi')

def add_book(books, isbn, title, author, genre, total_copies):
    if isbn in books:
        return False, "ISBN already exists."
    if genre not in GENRES:
        return False, f"Invalid genre. Valid genres: {', '.join(GENRES)}"
    books[isbn] = {
        'title': title,
        'author': author,
        'genre': genre,
        'total_copies': total_copies,
        'available_copies': total_copies
    }
    return True, "Book added successfully."

def add_member(members, member_id, name, email):
    if any(m['id'] == member_id for m in members):
        return False, "Member ID already exists."
    members.append({
        'id': member_id,
        'name': name,
        'email': email,
        'borrowed': []
    })
    return True, "Member added successfully."

def search_books(books, query):
    results = []
    for isbn, book in books.items():
        if (query.lower() in book['title'].lower() or
            query.lower() in book['author'].lower()):
            results.append((isbn, book))
    return results

def update_book(books, isbn, field, value):
    if isbn not in books:
        return False, "Book not found."
    book = books[isbn]
    if field == 'total_copies':
        try:
            new_total = int(value)
            book['total_copies'] = new_total
            book['available_copies'] = min(book['available_copies'], new_total)
            return True, "Book updated successfully."
        except ValueError:
            return False, "Total copies must be an integer."
    elif field == 'genre':
        if value not in GENRES:
            return False, f"Invalid genre. Valid genres: {', '.join(GENRES)}"
    try:
        book[field] = int(value) if field == 'total_copies' else value
        return True, "Book updated successfully."
    except ValueError:
        return False, "Invalid value for the field."

def update_member(members, member_id, field, value):
    for member in members:
        if member['id'] == member_id:
            if field not in ('name', 'email'):
                return False, "Field must be 'name' or 'email'."
            member[field] = value
            return True, "Member updated successfully."
    return False, "Member not found."

def delete_book(books, members, isbn):
    if isbn not in books:
        return False, "Book not found."
    borrowed_count = sum(1 for m in members if isbn in m['borrowed'])
    if borrowed_count > 0:
        return False, f"Cannot delete: {borrowed_count} copies borrowed."
    del books[isbn]
    return True, "Book deleted successfully."

def delete_member(members, books, member_id):
    for i, member in enumerate(members):
        if member['id'] == member_id:
            if member['borrowed']:
                return False, f"Cannot delete: {len(member['borrowed'])} books borrowed."
            del members[i]
            return True, "Member deleted successfully."
    return False, "Member not found."

def borrow_book(books, members, member_id, isbn):
    member = next((m for m in members if m['id'] == member_id), None)
    if not member:
        return False, "Member not found."
    if len(member['borrowed']) >= 3:
        return False, "Member has reached the 3-book limit."
    if isbn not in books:
        return False, "Book not found."
    if books[isbn]['available_copies'] <= 0:
        return False, "No copies available."
    member['borrowed'].append(isbn)
    books[isbn]['available_copies'] -= 1
    return True, "Book borrowed successfully."

def return_book(books, members, member_id, isbn):
    member = next((m for m in members if m['id'] == member_id), None)
    if not member:
        return False, "Member not found."
    if isbn not in member['borrowed']:
        return False, "Book not borrowed by this member."
    if isbn not in books:
        return False, "Book not found."
    member['borrowed'].remove(isbn)
    books[isbn]['available_copies'] += 1
    return True, "Book returned successfully."