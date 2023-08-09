import sqlite3

# Connect database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

def query_books_by_author(author_name):
    cursor.execute('''
        SELECT title, page_count, year_written, isbn
        FROM Books
        WHERE author = ?
    ''', (author_name,))
    books = cursor.fetchall()

    if not books:
        print(f"No books found by {author_name}.")
        return

    print(f"Books by {author_name}:")
    for book in books:
        title, page_count, year_written, isbn = book
        print(f"Author Name: {author_name}")
        print(f"Title: {title}")
        print(f"Page Count: {page_count}")
        print(f"Year Written: {year_written}")
        print(f"ISBN: {isbn}")
        print()

while True:
    author_name = input("Enter author's name (or 'exit' to quit): ")
    
    if author_name.lower() == 'exit':
        break
    
    query_books_by_author(author_name)

conn.close()

