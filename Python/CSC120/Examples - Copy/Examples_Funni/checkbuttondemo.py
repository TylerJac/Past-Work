import tkinter
import tkinter.messagebox


class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Check Button Demo")
        self.main_window.geometry("300x150")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.rb1 = tkinter.Checkbutton(self.top_frame, text="option 1", variable=self.cb_var1)
        self.rb2 = tkinter.Checkbutton(self.top_frame, text="option 2", variable=self.cb_var2)
        self.rb3 = tkinter.Checkbutton(self.top_frame, text="option 3", variable=self.cb_var3)

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

        message = "You selected:\n"

        if self.cb_var1.get() == 1:
            message += "1\n"
        if self.cb_var2.get() == 1:
            message += "2\n"
        if self.cb_var3.get() == 1:
            message += "3\n"

        tkinter.messagebox.showinfo("Selection", message)


if __name__ == '__main__':
    window = MyGUI()
