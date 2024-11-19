import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("me first GUI")

        self.label1 = tkinter.Label(self.main_window, text="Hello World", borderwidth=1, relief="solid")
        self.label2 = tkinter.Label(self.main_window, text="this is my gui program", borderwidth=2, relief="solid")

        self.label1.pack(ipadx=20, ipady=20, padx=20, pady=10)
        self.label2.pack(ipadx=20, ipady=20, padx=20, pady=10)

        tkinter.mainloop()


def main():
    main_gui = MyGUI()

    tkinter.mainloop()


if __name__ == '__main__':
    main()
