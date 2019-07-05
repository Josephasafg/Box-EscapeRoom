from tkinter import *
from tkinter import ttk
from StartPage import StartPage
from PageOne import PageOne
LARGE_FONT = ("verdana", 14)


class CountDown(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        container = Frame(self, width=width, height=height)
        container.grid_propagate(False)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = dict()

        for f in (StartPage, PageOne):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(StartPage)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()