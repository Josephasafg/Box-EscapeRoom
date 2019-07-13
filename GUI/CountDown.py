from tkinter import *
from GUI.StartPage import StartPage
from Utils.Utilities import resource_path

LARGE_FONT = ("verdana", 14)


class CountDown(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        position_right = int(self.winfo_screenwidth() / 2 - width / 2)
        position_down = int(self.winfo_screenheight() / 2 - height / 2)
        self.geometry(f"+{position_right}+{position_down}")
        self.wm_iconbitmap(resource_path('Images/Max-logo.ico'))
        self.container = Frame(self, width=width, height=height)
        self.container.grid_propagate(False)
        self.container.pack(side=TOP, fill=BOTH, expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = dict()

        frame = StartPage(self.container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(StartPage)

    def add_class_to_tuple(self, class_name):
        frame = class_name(self.container, self)
        self.frames[class_name] = frame
        frame.grid(row=0, column=0, sticky=NSEW)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
