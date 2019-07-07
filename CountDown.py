from tkinter import *
from tkinter import ttk
from StartPage import StartPage
from DropDown import DropDown
from GroupNamingPage import GroupNamingPage
from Game import Game
LARGE_FONT = ("verdana", 14)


class CountDown(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.container = Frame(self, width=width, height=height)
        self.container.grid_propagate(False)
        self.container.pack(side=TOP, fill=BOTH, expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = dict()

        for f in (StartPage, Game, DropDown):
            frame = f(self.container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(StartPage)

    def add_class_to_tuple(self, class_name):
        frame = class_name(self.container, self)
        self.frames[class_name] = frame
        frame.grid(row=0, column=0, sticky=NSEW)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()