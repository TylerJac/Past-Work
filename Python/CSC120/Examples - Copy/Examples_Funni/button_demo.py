import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("button demo")

        self.my_button = tkinter.Button(self.main_window, text="CLICK ME", command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text="quit", command=self.main_window.destroy)

        self.my_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("response", "thanks for clicking button")


if __name__ == '__main__':
    main_gui = MyGUI()
