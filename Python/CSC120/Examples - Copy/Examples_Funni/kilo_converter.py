import tkinter
import tkinter.messagebox


class KiloConverterGUI:

    def __init__(self):
        self.root = tkinter.Tk()

        self.root.title("Kilo convert")

        self.top_frame = tkinter.Frame(self.root)
        self.mid_frame = tkinter.Frame(self.root)
        self.bottem_frame = tkinter.Frame(self.root)

        self.prompt = tkinter.Label(self.top_frame, text="Enter distance:")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.descr_label = tkinter.Label(self.mid_frame, text="Converted to miles: ")

        self.result = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.result)

        self.descr_label.pack(side="left")
        self.miles_label.pack(side="left")

        self.calc_button = tkinter.Button(self.bottem_frame, text="convert", command=self.convert)
        self.quit = tkinter.Button(self.bottem_frame, text="quit", command=self.root.destroy)

        self.calc_button.pack(side="left")
        self.quit.pack(side="left")

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottem_frame.pack()
        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214

        # tkinter.messagebox.showinfo("results", f"{kilo} kilo is equal to {miles} miles.")
        self.result.set(str(miles))


if __name__ == "__main__":
    kilo_conv = KiloConverterGUI()
