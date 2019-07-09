from tkinter import *
from tkinter import ttk
from Game import Game
from GroupNamingPage import GroupNamingPage

OPTIONS = ["5 minutes", "10 minutes", "15 minutes"]

LARGE_FONT = ("verdana", 16)
MEDIUM_FONT = ("verdana", 10)


class DropDown(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='black')
        box_name = Label(self, text="Choose amount of penalty in minutes:", font=LARGE_FONT, fg='white', bg='black')
        box_name.pack(fill=X, padx=10, pady=10)
        self.current_table = StringVar()
        comboExample = ttk.Combobox(self, textvariable=self.current_table, state="readonly",
                                    values=OPTIONS)
        comboExample.pack(padx=10, pady=10)
        comboExample.current(0)
        next_button = ttk.Button(self, text="Next",
                                 command=lambda: self.go_to_next_page(self.current_table.get()))
        next_button.pack(padx=10, pady=10)
    #     TODO: place button on bottom right

    def parse_value(self, combo_value: str) -> int:
        minute = [int(s) for s in combo_value.split() if s.isdigit()]
        return minute[0] * 60

    def go_to_next_page(self, combo_value):
        seconds = self.parse_value(combo_value)
        Game.penalty = seconds
        self.controller.add_class_to_tuple(GroupNamingPage)
        self.controller.show_frame(GroupNamingPage)



