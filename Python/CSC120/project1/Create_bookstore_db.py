# create_bookstore_db.py

import sqlite3

def create_bookstore_db():
    conn = sqlite3.connect("bookstore.db")
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS Books
                 (ISBN INTEGER PRIMARY KEY, 
                 Title TEXT, 
                 Author TEXT, 
                 Edition INTEGER, 
                 Price REAL, 
                 Publisher TEXT)''')

    # Insert some data
    books_data = [
        (1234567890, 'Book1', 'Author1', 1, 19.99, 'Publisher1'),
        (2345678901, 'Book2', 'Author2', 2, 29.99, 'Publisher2'),
        # Add more data here...
    ]
    c.executemany('INSERT INTO Books VALUES (?, ?, ?, ?, ?, ?)', books_data)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_bookstore_db()
