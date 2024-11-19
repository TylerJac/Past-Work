# interface.py

import tkinter as tk
from tkinter import messagebox
from database import BookstoreDB

class BookstoreUI:
    def __init__(self, master):
        self.master = master
        self.master.title("CFCC Bookstore Book Inventory Management System")
        self.master.geometry("900x500")
        
        self.db = BookstoreDB("bookstore.db")
        
        # Labels
        self.lbl_isbn = tk.Label(master, text="ISBN:")
        self.lbl_isbn.grid(row=0, column=0, sticky="e")
        
        self.lbl_title = tk.Label(master, text="Title:")
        self.lbl_title.grid(row=1, column=0, sticky="e")
        
        self.lbl_author = tk.Label(master, text="Author:")
        self.lbl_author.grid(row=2, column=0, sticky="e")
        
        self.lbl_edition = tk.Label(master, text="Edition:")
        self.lbl_edition.grid(row=3, column=0, sticky="e")
        
        self.lbl_price = tk.Label(master, text="Price:")
        self.lbl_price.grid(row=4, column=0, sticky="e")
        
        self.lbl_publisher = tk.Label(master, text="Publisher:")
        self.lbl_publisher.grid(row=5, column=0, sticky="e")
        
        # Entries
        self.ent_isbn = tk.Entry(master)
        self.ent_isbn.grid(row=0, column=1)
        
        self.ent_title = tk.Entry(master)
        self.ent_title.grid(row=1, column=1)
        
        self.ent_author = tk.Entry(master)
        self.ent_author.grid(row=2, column=1)
        
        self.ent_edition = tk.Entry(master)
        self.ent_edition.grid(row=3, column=1)
        
        self.ent_price = tk.Entry(master)
        self.ent_price.grid(row=4, column=1)
        
        self.ent_publisher = tk.Entry(master)
        self.ent_publisher.grid(row=5, column=1)
        
        # Buttons
        self.btn_create = tk.Button(master, text="Create", command=self.create_book)
        self.btn_create.grid(row=6, column=0)

        self.btn_save = tk.Button(master, text="Save Records", command=self.save_records)
        self.btn_save.grid(row=6, column=1)

        self.btn_clear = tk.Button(master, text="Clear", command=self.clear_entries)
        self.btn_clear.grid(row=6, column=2)
        
        self.btn_read = tk.Button(master, text="Read", command=self.read_book)
        self.btn_read.grid(row=6, column=3)
        
        self.btn_update = tk.Button(master, text="Update", command=self.update_book)
        self.btn_update.grid(row=6, column=4)
        
        self.btn_delete = tk.Button(master, text="Delete", command=self.delete_book)
        self.btn_delete.grid(row=6, column=5)
        
        self.btn_exit = tk.Button(master, text="Exit", command=master.quit)
        self.btn_exit.grid(row=8, column=1)
        
        # Inventory Listbox
        self.lst_inventory = tk.Listbox(master, width=80)
        self.lst_inventory.grid(row=7, columnspan=4)
        
    def create_book(self):
        isbn = self.ent_isbn.get()
        title = self.ent_title.get()
        author = self.ent_author.get()
        edition = self.ent_edition.get()
        price = self.ent_price.get()
        publisher = self.ent_publisher.get()
        
        try:
            # Convert edition to int and price to float
            edition = int(edition)
            price = float(price)
            
            # Call create_book method of BookstoreDB
            self.db.create_book(isbn, title, author, edition, price, publisher)
            
            # Show success message
            messagebox.showinfo("Success", "Book created successfully!")
            
            # Clear entry fields
            self.clear_entries()
            
            # Update inventory listbox
            self.populate_inventory()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid edition and price.")
    
    def read_book(self):
        # Clear inventory listbox
        self.lst_inventory.delete(0, tk.END)
        
        # Get all books from database
        books = self.db.read_all_books()
        
        # Display each book in the inventory listbox
        for book in books:
            self.lst_inventory.insert(tk.END, f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}, Edition: {book[3]}, Price: {book[4]}, Publisher: {book[5]}")
            
    def update_book(self):
        # Get ISBN from entry field
        isbn = self.ent_isbn.get()
        
        # Check if ISBN is provided
        if not isbn:
            messagebox.showerror("Error", "Please enter ISBN to update.")
            return
        
        # Get book details from entry fields
        title = self.ent_title.get()
        author = self.ent_author.get()
        edition = self.ent_edition.get()
        price = self.ent_price.get()
        publisher = self.ent_publisher.get()
        
        try:
            # Convert edition to int and price to float
            edition = int(edition)
            price = float(price)
            
            # Call update_book method of BookstoreDB
            self.db.update_book(isbn, title, author, edition, price, publisher)
            
            # Show success message
            messagebox.showinfo("Success", "Book updated successfully!")
            
            # Clear entry fields
            self.clear_entries()
            
            # Update inventory listbox
            self.populate_inventory()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid edition and price.")
    
    def delete_book(self):
        # Get ISBN from entry field
        isbn = self.ent_isbn.get()
        
        # Check if ISBN is provided
        if not isbn:
            messagebox.showerror("Error", "Please enter ISBN to delete.")
            return
        
        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this book?")
        if not confirm:
            return
        
        # Call delete_book method of BookstoreDB
        self.db.delete_book(isbn)
        
        # Show success message
        messagebox.showinfo("Success", "Book deleted successfully!")
        
        # Clear entry fields
        self.clear_entries()
        
        # Update inventory listbox
        self.populate_inventory()
    
    def clear_entries(self):
        # Clear all entry fields
        self.ent_isbn.delete(0, tk.END)
        self.ent_title.delete(0, tk.END)
        self.ent_author.delete(0, tk.END)
        self.ent_edition.delete(0, tk.END)
        self.ent_price.delete(0, tk.END)
        self.ent_publisher.delete(0, tk.END)

    def save_records(self):
        # Call create_book method to save the book
        self.create_book()

    def clear_entries_bottom(self):
        # Clear entry fields at the bottom right
        self.ent_isbn.delete(0, tk.END)
        self.ent_title.delete(0, tk.END)
        self.ent_author.delete(0, tk.END)
        self.ent_edition.delete(0, tk.END)
        self.ent_price.delete(0, tk.END)
        self.ent_publisher.delete(0, tk.END)

    def populate_inventory(self):
        # Clear inventory listbox
        self.lst_inventory.delete(0, tk.END)
        
        # Get all books from database
        books = self.db.read_all_books()
        
        # Display each book in the inventory listbox
        for book in books:
            self.lst_inventory.insert(tk.END, f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}, Edition: {book[3]}, Price: {book[4]}, Publisher: {book[5]}")
