import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("me first GUI")

        self.label1 = tkinter.Label(self.main_window, text="Hello World", borderwidth=1, relief="solid")
        self.label2 = tkinter.Label(self.main_window, text="this is my gui program", relief="groove")

        self.label1.pack(side="left")
        self.label2.pack(side="left")

        tkinter.mainloop()


def main():
    main_gui = MyGUI()

    tkinter.mainloop()


if __name__ == '__main__':
    main()
