import sqlite3
from pprint import pprint

# Connect to the database or create a new one
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Create a table to store books
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY,
        author TEXT NOT NULL,
        title TEXT NOT NULL,
        page_count INTEGER,
        year_written INTEGER,
        isbn TEXT
    )
''')

# Sample data for Albert Camus' books
camus_books_data = [
    ("Albert Camus", "The Stranger", 123, 1942, "978-0-394-40166-1"),
    ("Albert Camus", "The Myth of Sisyphus", 256, 1942, "978-0-679-73373-7"),
    ("Albert Camus", "The Plague", 308, 1947, "978-0-679-72021-8"),
    ("Albert Camus", "The Fall", 147, 1956, "978-0-679-72021-8"),
    ("Albert Camus", "Exile and the Kingdom", 213, 1957, "978-0-394-40087-9"),
]

# Sample data for Karl Marx's books
marx_books_data = [
    ("Karl Marx", "The Communist Manifesto", 52, 1848, "978-0-486-20284-4"),
    ("Karl Marx", "Das Kapital", 1152, 1867, "978-0-486-20284-4"),
    ("Karl Marx", "The Eighteenth Brumaire of Louis Napoleon", 168, 1852, "978-0-486-20284-4"),
]

# Sample data for Friedrich Nietzsche's books
nietzsche_books_data = [                                                               # list, series of items surrounded by [brackets]
    ("Friedrich Nietzsche", "Thus Spoke Zarathustra", 352, 1883, "978-0-14-044118-5"), # tuple
    ("Friedrich Nietzsche", "Beyond Good and Evil", 240, 1886, "978-0-14-044923-5"),   # tuple
    ("Friedrich Nietzsche", "Ecce Homo", 144, 1908, "978-0-14-044515-2"),              # tuple basically a list surround by (parentheses)
         # 0                   1          2     3        4
         # 0 = author
         # 1 = title
         # 2 = page length
         # 3 = year published
         # 4 = ISBN number
]

# Insert sample data into the Books table create one giant list of tuples
all_books_data = camus_books_data + marx_books_data + nietzsche_books_data

pprint(all_books_data)
print(type(all_books_data))

cursor.executemany('''
    INSERT INTO Books (author, title, page_count, year_written, isbn)
    VALUES (?, ?, ?, ?, ?)
''', all_books_data)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()

print("Database with books created successfully!")

