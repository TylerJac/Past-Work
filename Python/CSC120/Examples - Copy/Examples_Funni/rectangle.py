import tkinter


class MyGUI:

    def __init__(self):
        self.root = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.root, width=200, height=200)
        self.canvas.create_rectangle(10, 10, 199, 199)
        self.canvas.pack()

        tkinter.mainloop()


if __name__ == '__main__':
    window = MyGUI()
