from tkinter import *
from tkinter import ttk
from Game import Game

OPTIONS = ["5 minutes", "10 minutes", "15 minutes"]

LARGE_FONT = ("verdana", 14)
MEDIUM_FONT = ("verdana", 10)


class DropDown(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        box_name = Label(self, text="Choose amount of penalty in minutes:", font=LARGE_FONT)
        box_name.pack(fill=X)
        self.current_table = StringVar()
        # comboExample = ttk.Combobox(self, values=OPTIONS)
        comboExample = ttk.Combobox(self, textvariable=self.current_table, state="readonly",
                                    values=OPTIONS)
        comboExample.pack()
        comboExample.current(1)
        next_button = ttk.Button(self, text="Next",
                                 command=lambda: self.go_to_next_page(self.current_table.get()))
        next_button.pack()
    #     TODO: place button on bottom right

    def parse_value(self, combo_value: str) -> int:
        minute = [int(s) for s in combo_value.split() if s.isdigit()]
        return minute[0] * 60

    def go_to_next_page(self, combo_value):
        seconds = self.parse_value(combo_value)
        Game.penalty = seconds
        self.controller.show_frame(Game)



