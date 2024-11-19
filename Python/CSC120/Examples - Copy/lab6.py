# ===============================================================

# Name: Tyler Jackson

# Date: 4/22/2024

# Course: CSC 120 NLE01

# Algorithm:Import necessary libraries,
# Define the StudentInfo class,
# Define the entry point,


# References: in class

# ===============================================================

import tkinter as tk

class StudentInfo:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Lab 6: GUI Programming")

        # Variables to hold student information
        self.name = "Tyler Jackson"
        self.course_number = "CSC 120 NLE01"
        self.degree_path = "IT Associate's Degree"

        # Label to display student information
        self.info_label = tk.Label(self.window, text="", padx=20, pady=10)
        self.info_label.pack()

        # Button to show student information
        self.show_info_button = tk.Button(self.window, text="Show Info", command=self.show_info)
        self.show_info_button.pack()

        # Button to quit the program
        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.quit)
        self.quit_button.pack()

        # Adjust window size
        self.window.geometry("300x150")

        # Start the Tkinter event loop
        self.window.mainloop()

    def show_info(self):
        # Update label with student information
        self.info_label.config(text=f"Name: {self.name}\nCourse Number: {self.course_number}\nDegree Path: {self.degree_path}")

if __name__ == "__main__":
    student_info_app = StudentInfo()
