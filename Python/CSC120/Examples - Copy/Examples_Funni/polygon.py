import tkinter


class MyGUI:

    def __init__(self):
        self.root = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.root, width=200, height=200)
        self.canvas.create_polygon(60, 20, 100, 20, 140, 60, 140, 100, 100, 140, 60, 140, 20, 100, 20, 60)
        self.canvas.pack()

        tkinter.mainloop()


if __name__ == '__main__':
    window = MyGUI()
