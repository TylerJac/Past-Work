import tkinter
import tkinter.messagebox


class MyGUI:

    def __init__(self):
        self.root = tkinter.Tk()

        self.root.title("DropDown Demo")
        self.root.geometry("350x150")

        self.top_frame = tkinter.Frame(self.root)
        self.bottom_frame = tkinter.Frame(self.root)

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        self.option = tkinter.StringVar()

        self.option.set(days[0])

        self.option_menu = tkinter.OptionMenu(self.top_frame, self.option, *days)
        self.option_menu.config(width=20)

        self.option_menu.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text="OK", command=self.show_choice)
        self.quit_but = tkinter.Button(self.bottom_frame, text="quit", command=self.root.destroy)

        self.ok_button.pack(side="left")
        self.quit_but.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        message = f"You selected:\n{self.option.get()}"

        tkinter.messagebox.showinfo("Selection", message)


if __name__ == '__main__':
    window = MyGUI()
