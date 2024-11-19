# database.py

import sqlite3

class DBMS:
    def __init__(self, name):
        self.name = name
        self.__connection = sqlite3.connect(self.name)
        
    def __enter__(self):
        return self.__connection.cursor()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.commit()
        self.__connection.close()

class BookstoreDB:
    def __init__(self, db_name):
        self.db_name = db_name
        
    def create_book(self, isbn, title, author, edition, price, publisher):
        with DBMS(self.db_name) as cursor:
            cursor.execute("INSERT INTO Books VALUES (?, ?, ?, ?, ?, ?)",
                           (isbn, title, author, edition, price, publisher))
            
    def read_book(self, isbn):
        with DBMS(self.db_name) as cursor:
            cursor.execute("SELECT * FROM Books WHERE ISBN=?", (isbn,))
            return cursor.fetchone()
        
    def read_all_books(self):
        with DBMS(self.db_name) as cursor:
            cursor.execute("SELECT * FROM Books")
            return cursor.fetchall()
        
    def update_book(self, isbn, title, author, edition, price, publisher):
        with DBMS(self.db_name) as cursor:
            cursor.execute("UPDATE Books SET Title=?, Author=?, Edition=?, Price=?, Publisher=? WHERE ISBN=?",
                           (title, author, edition, price, publisher, isbn))
            
    def delete_book(self, isbn):
        with DBMS(self.db_name) as cursor:
            cursor.execute("DELETE FROM Books WHERE ISBN=?", (isbn,))
