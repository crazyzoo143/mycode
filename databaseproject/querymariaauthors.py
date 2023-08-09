import sqlite3

# Connect to the database no data base no work
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

def query_books_by_author(author_name):
    cursor.execute('''
        SELECT title, page_count, year_written, isbn
        FROM Books
        WHERE author = ?
    ''', (author_name,))
    books = cursor.fetchall()

    #print(f"Books by {author_name}:")
    for book in books:
        title, page_count, year_written, isbn = book
        print(f"Author: {author_name}")
        print(f"Title: {title}")
        print(f"Page Count: {page_count}")
        print(f"Year Written: {year_written}")
        print(f"ISBN: {isbn}")
        print()

# Look up the books by the  authors in database 
query_books_by_author("Albert Camus")
query_books_by_author("Karl Marx")
query_books_by_author("Friedrich Nietzsche")

conn.close()

