import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("frame demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text="Winken")
        self.label2 = tkinter.Label(self.top_frame, text="Blinken")
        self.label3 = tkinter.Label(self.top_frame, text="nod")

        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")

        self.label1 = tkinter.Label(self.bottom_frame, text="Winken")
        self.label2 = tkinter.Label(self.bottom_frame, text="Blinken")
        self.label3 = tkinter.Label(self.bottom_frame, text="nod")

        self.label1.pack(side="left")
        self.label2.pack(side="left")
        self.label3.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


def main():
    main_gui = MyGUI()

    tkinter.mainloop()


if __name__ == '__main__':
    main()
