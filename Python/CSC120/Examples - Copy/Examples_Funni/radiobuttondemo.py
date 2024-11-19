import tkinter
import tkinter.messagebox


class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("radio Button Demo")
        self.main_window.geometry("300x150")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text="option 1", variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text="option 2", variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text="option 3", variable=self.radio_var, value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text="OK", font=("Arial", 25), background="blue",
                                        activebackground="red",
                                        highlightbackground="green",
                                        activeforeground="yellow", command=self.show_choice)
        self.quit_but = tkinter.Button(self.bottom_frame, text="quit", font=("Wingdings", 25),
                                       command=self.main_window.destroy)

        self.ok_button.pack(side="left")
        self.quit_but.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("Selection", f"You select your option {self.radio_var.get()}")


if __name__ == '__main__':
    window = MyGUI()
